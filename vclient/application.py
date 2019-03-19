import logging
import pickle
from typing import NamedTuple

import commands
import pika
import settings
from common.common import CommandMessage, ResultMessage
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.channel import Channel

log = logging.getLogger(__name__)


def get_name_queue():
    import urllib.request
    ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
    return ip


class Application:
    def __init__(self):
        self.connectionParameters = pika.ConnectionParameters(settings.SERVER_IP, 5672)

        self.connection: BlockingConnection = None
        self.channel: BlockingChannel = None

        self.queue_name = get_name_queue()

    def connect(self):
        self.connection = BlockingConnection(pika.ConnectionParameters(settings.SERVER_IP, settings.SERVER_PORT))

        log.debug('RabbitMQ connect')

        self.channel = self.connection.channel()

        self.channel.queue_declare(self.queue_name, auto_delete=True)

        self.channel.basic_consume(self.handler_commands, self.queue_name)

        log.debug('RabbitMQ listen')

        self.channel.start_consuming()

    def handler_commands(self, channel: Channel, method, properties: BasicProperties, body):
        log.debug('Message received')

        channel.basic_ack(method.delivery_tag)

        properties = BasicProperties(
            correlation_id=properties.correlation_id,
            type='result',
            app_id=self.queue_name
        )

        message: CommandMessage = self.deserialize(body)

        if not isinstance(message, CommandMessage):
            log.error('Invalid CommandMessage: %s', message)
            return

        log.debug('Command: %s', message.command)
        log.debug('Parameters: %s', message.parameters)

        result: ResultMessage = self.call_command(message.command, message.parameters)

        log.debug('Result command: %s', result)

        channel.basic_publish('', 'worker', self.serialize(result), properties=properties)

        log.debug('Send result')

    def call_command(self, command: str, parameters: NamedTuple = None) -> ResultMessage:
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

        return ResultMessage('INVALID_COMMAND')

    def deserialize(self, data):
        return pickle.loads(data)

    def serialize(self, data):
        return pickle.dumps(data)
