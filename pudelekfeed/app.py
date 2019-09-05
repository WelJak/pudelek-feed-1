import time
import uuid
import json

from pudelekfeed.checker.inmemory_checker import *
from pudelekfeed.rabbitmq_producer.rabbitmq_producer import *
from pudelekfeed.scrapper.scrapper import *

try:
    with open('definitions.json') as config_file:
        data = json.load(config_file)

    LOGIN = data['users'][0]['name']
    PASSWORD = data['users'][0]['password']
    # HOST = trzeba bedzie dodac do pliku konfiguracyjnego
    EXCHANGE = data['exchanges'][0]['name']
    VHOST = data['bindings'][0]['vhost']
    ROUTING_KEY = data['bindings'][0]['destination']
except Exception:
    logger.info('An error occurred during processing config file:')
    traceback.print_exc(file=sys.stdout)

FEED_TYPE = 'PUDELEK'
SLEEP_TIME_IN_SECONDS = 5
WEBSITE_URL = 'https://www.pudelek.pl'


class App:

    def main(self):
        try:
            scrapper = Scrapper(WEBSITE_URL)
            checker = InMemoryChecker()
            producer = RabbitmqProducer(LOGIN, PASSWORD, 'localhost', EXCHANGE, VHOST, ROUTING_KEY) #pozniej zamiast 'localhost' -> zmienna HOST
            while 1:
                news = scrapper.fetch_news_from_website()
                news_to_send = list(filter(lambda message: checker.check(message), news))
                messages = list(map(lambda message: self.create_message(message), news_to_send))
                for msg in messages:
                    response = producer.send_message(msg)
                    if response:
                        checker.mark(msg['message'])
                time.sleep(SLEEP_TIME_IN_SECONDS)
        except Exception as e:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)

    def create_message(self, message):
        return {'uuid': str(uuid.uuid1()), 'type': FEED_TYPE, 'message': message}


x = App()
x.main()
