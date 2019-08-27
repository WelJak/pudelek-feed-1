from scrapper import fetch_list_of_entries
import pika
import json


class RabbitSend():

    def send_messages(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        #channel.queue_declare(queue='pudelek')
        entries = fetch_list_of_entries()
        for entry in entries:
            body = json.dumps(entry)
            channel.basic_publish(exchange='',
                                  routing_key='pudelek',
                                  body=body)
            print('message sent')
        connection.close()

if __name__ == '__main__':
    x = RabbitSend()
    x.send_messages()