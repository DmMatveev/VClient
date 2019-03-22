import logging
import pickle
import time
from typing import NamedTuple

import commands
import pika
import requests
import settings
from common.common import CommandMessage, ResultMessage, CommandStatus
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.channel import Channel
from pika.exceptions import ConnectionClosed, IncompatibleProtocolError

log = logging.getLogger(__name__)


class ApplicationUpdate(Exception):
    pass


class Application:
    RESULT_QUEUE = 'worker'

    def __init__(self):
        self.connectionParameters = pika.ConnectionParameters(settings.SERVER_IP, 5672)

        self.connection: BlockingConnection = None
        self.channel: BlockingChannel = None

        self.queue_name = ''

    def connect(self):
        if self.connection is None or self.connection.is_closed:
            self.connection = BlockingConnection(pika.ConnectionParameters(settings.SERVER_IP, settings.SERVER_PORT))

        self.queue_name = self.get_name_queue()

        log.debug('RabbitMQ connect')

        self.channel = self.connection.channel()

        self.channel.queue_declare(self.queue_name, auto_delete=True)

        self.channel.basic_consume(self.handler_command, self.queue_name)

        log.debug('RabbitMQ listen')

        self.channel.start_consuming()

    def handler_command(self, channel: Channel, method, properties: BasicProperties, body):
        channel.basic_ack(method.delivery_tag)

        properties = BasicProperties(
            correlation_id=properties.correlation_id,
            type='result',
            app_id=self.queue_name
        )

        message: CommandMessage = self.deserialize(body)

        if not isinstance(message, CommandMessage):
            log.error('Invalid CommandMessage: %s', message)
            channel.basic_publish('',
                                  self.RESULT_QUEUE,
                                  self.serialize(ResultMessage(CommandStatus.INVALID)),
                                  properties=properties)
            return

        log.debug('Command: %s', message.command)

        if message.command == 'application.update':
            channel.basic_publish('',
                                  self.RESULT_QUEUE,
                                  self.serialize(ResultMessage(CommandStatus.SUCCESS)),
                                  properties=properties)

            raise ApplicationUpdate

        result: ResultMessage = self.call_command(message.command, message.parameters)

        log.debug('Result command: %s', result)

        channel.basic_publish('', self.RESULT_QUEUE, self.serialize(result), properties=properties)

    @staticmethod
    def call_command(command: str, parameters: NamedTuple = None) -> ResultMessage:
        command = command.lower()

        command_type, command = command.split('.')

        directory = getattr(commands, command_type)
        file = getattr(directory, command)
        command = getattr(file, command.capitalize())

        if command.RPC:
            if parameters:
                result = command(parameters).message
            else:
                result = command().message

            return result

        return ResultMessage(CommandStatus.ERROR)

    @staticmethod
    def deserialize(data):
        return pickle.loads(data)

    @staticmethod
    def serialize(data):
        return pickle.dumps(data)

    @staticmethod
    def get_name_queue():
        #request = requests.get('', params={'uuid': '123'})
        '''
            if успешно:
                return name

            ip адресс

        '''

        import urllib.request
        ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
        return ip

    def start(self):
        while True:
            try:
                self.connect()
            except ConnectionClosed:
                log.debug('RabbitMQ connection broken')
                time.sleep(30)

            except IncompatibleProtocolError:
                log.debug('RabbitMQ connection broken')
                time.sleep(30)

            except ApplicationUpdate:
                log.debug('Application update')
                self.channel.close()
