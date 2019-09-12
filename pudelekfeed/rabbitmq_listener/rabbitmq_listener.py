import pika
import logger
import json

class RabbitmqListener:

    def __init__(self, login, password, host, exchange, virtual_host, routing_key, queue_name):
        self.credentials = pika.PlainCredentials(login, password)
        self.host = host
        self.exchange = exchange
        self.port = 5672
        self.virtual_host = virtual_host
        self.routing_key = routing_key
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()

    logger.info('Waiting for messages from pudelek-feed')
    @staticmethod
    def callback(ch, method, properties, body):
        logger.info('received {}'.format(json.loads(body)))

    def start_listening(self):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True
        )
        self.channel.start_consuming()

listener = RabbitmqListener('admin', 'admin', 'localhost', 'feed-exchange', 'PUDELEK', 'PUDELEK', 'pudelek-feed')
listener.start_listening()
