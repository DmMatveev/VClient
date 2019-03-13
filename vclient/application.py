import logging
import pickle
from typing import Any, Dict

import pika
import settings
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.channel import Channel

import commands

logger = logging.getLogger(__name__)


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

        print('Connected')

        self.channel = self.connection.channel()

        self.channel.queue_declare(self.queue_name, auto_delete=True)

        self.channel.basic_consume(self.handler_commands, self.queue_name)

        print('Listen')

        self.channel.start_consuming()

    def handler_commands(self, channel: Channel, method, properties: BasicProperties, body):
        properties = BasicProperties(
            correlation_id=properties.correlation_id,
            type='result',
            app_id=self.queue_name
        )

        message = self.deserialize(body)

        print(message)

        result = self.call_command(**message)

        print(result)

        channel.basic_publish('', 'worker', self.serialize(result), properties=properties)

    def call_command(self, command: str, arguments: Dict = None):
        arguments = arguments or {}

        command = command.lower()

        command_type, command = command.split('.')

        directory = getattr(commands, command_type)
        file = getattr(directory, command)
        command = getattr(file, command.capitalize())

        if command.RPC:
            return command(**arguments).result

        return 'INVALID_COMMAND'

    def deserialize(self, data):
        return pickle.loads(data)

    def serialize(self, data):
        return pickle.dumps(data)
