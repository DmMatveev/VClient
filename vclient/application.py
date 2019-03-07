import importlib
import pickle
from functools import partial
from typing import Any

import pika
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.channel import Channel

from vclient import commands


def get_name_queue():
    import urllib.request
    ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
    return '6'
    return ip


class Application:
    def __init__(self):
        self.connection: BlockingConnection = BlockingConnection(pika.ConnectionParameters('localhost', 5672))
        self.channel: BlockingChannel = self.connection.channel()

        queue_name = get_name_queue()

        self.channel.queue_declare(queue_name, auto_delete=True)

        self.channel.basic_consume(self.handler_commands, queue_name)

        self.channel.start_consuming()

    def handler_commands(self, channel: Channel, method, properties: BasicProperties, body):
        properties = BasicProperties(
            correlation_id=properties.correlation_id,
            type='result'
        )

        command = self.deserialize(body)

        result = self.call_command(command)

        channel.basic_publish('', 'worker', pickle.dumps(result), properties=properties)

    def call_command(self, command: str):
        command = command.lower()

        command_type, command = command.split('.')

        directory = getattr(commands, command_type)
        file = getattr(directory, command)
        command = getattr(file, command.capitalize())

        if command.RPC:
            return command().result

        return 'InvalidCommand'


    def deserialize(self, data: bytes) -> Any:
        return pickle.loads(data)

    def serialize(self, data: Any) -> bytes:
        return pickle.dumps(data)
