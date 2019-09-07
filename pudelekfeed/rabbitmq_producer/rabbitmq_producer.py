import json
import sys
import traceback

import pika

import logger


class RabbitmqProducer:

    def __init__(self, login, password, host, exchange, virtual_host, routing_key):
        self.credentials = pika.PlainCredentials(login, password)
        self.host = host
        self.exchange = exchange
        self.port = 5672
        self.virtual_host = virtual_host
        self.routing_key = routing_key
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()

    def send_message(self, message):
        try:
            body = json.dumps(message, ensure_ascii=False)
            self.channel.basic_publish(exchange=self.exchange,
                                       routing_key=self.routing_key,
                                       body=body)
            logger.info('Message: {} has been sent'.format(message))
            return True
        except:
            logger.info('An error occurred during sending message {}'.format(message))
            traceback.print_exc(file=sys.stdout)
            self.restart_connection()
            return False

    def connection_close(self):
        self.connection.close()

    def restart_connection(self):
        self.connection.close()
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()
