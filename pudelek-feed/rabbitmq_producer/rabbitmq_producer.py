
import pika
import json


class RabbitmqProducer():

    def __init__(self, login, password, host, port, virtual_host, routing_key):
        self.credentials = pika.PlainCredentials(login, password)
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.routing_key = routing_key
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials,
                                      virtual_host=self.virtual_host))
        self.channel = self.connection.channel()

    def send_message(self, message):
        try:
            body = json.dumps(message)
            self.channel.basic_publish(exchange='',
                                      routing_key=self.routing_key,
                                      body=body)
            print('message sent')
            return True
        except:
            print('something went wrong')
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


