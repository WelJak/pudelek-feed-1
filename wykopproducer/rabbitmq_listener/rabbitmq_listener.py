import json
import sys
import traceback

import pika

import logger


class RabbitmqListener:

    def __init__(self, login, password, host, exchange, virtual_host, queue_name):
        self.credentials = pika.PlainCredentials(login, password)
        self.host = host
        self.exchange = exchange
        self.port = 5672
        self.virtual_host = virtual_host
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()
        logger.info('Waiting for messages from pudelek-feed queue')

    def listen(self, function):
        try:
            def on_message_callback(ch, method, properties, body):
                function(json.loads(body))

            self.channel.basic_consume(queue=self.queue_name,
                                       on_message_callback=on_message_callback,
                                       auto_ack=True)
            self.channel.start_consuming()
        except Exception as e:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)
            raise e

    def restart_connection(self):
        if not self.connection.is_closed():
            self.connection.close()
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()
