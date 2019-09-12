from unittest import mock

import pika

import logger

mock = mock.Mock()


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

    logger.info('Waiting for messages from pudelek-feed')

    def listen(self, function):
        def on_message_callback(ch, method, properties, body):
            function(body)

        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=on_message_callback,
                                   auto_ack=True)
        self.channel.start_consuming()


class App:
    def logic(self, message):
        self.wykopInterface = mock
        self.wykopInterface.send_news_to_wykop(message)
        self.wykopInterface.send_news_to_wykop.return_value = logger.info(
            'Message has been successfully sent to wykop.pl')

    def main(self):
        rabbitListener = RabbitmqListener('admin', 'admin', 'localhost', 'feed-exchange', 'PUDELEK', 'pudelek-feed')
        rabbitListener.listen(self.logic)


x = App()
x.main()
