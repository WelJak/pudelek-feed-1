import configparser
import os
import time
import uuid

from checker.inmemory_checker import *
from rabbitmq_producer.rabbitmq_producer import *
from scrapper.scrapper import *

RABBIT_HOST = 'RABBIT_HOST'
RABBIT_LOGIN = 'RABBIT_LOGIN'
RABBIT_PASSWORD = 'RABBIT_PASSWORD'
RABBIT_EXCHANGE = 'RABBIT_EXCHANGE'
RABBIT_VHOST = 'RABBIT_VHOST'
RABBIT_ROUTING_KEY = 'RABBIT_ROUTING_KEY'
CONFIG_FILE = "variables.ini"

FEED_TYPE = 'PUDELEK'
SLEEP_TIME_IN_SECONDS = 'SLEEP_TIME_IN_SECONDS'
WEBSITE_URL = 'https://www.pudelek.pl'


class App:

    def main(self):
        profile = os.getenv('ENVIRONMENT', "LOCAL")
        logger.info("Running pudelek feed with active profile: " + profile)
        host, login, password, exchange, vhost, routing_key, sleep_time_in_seconds = self.read_config_file(profile)
        try:
            scrapper = Scrapper(WEBSITE_URL)
            checker = InMemoryChecker()
            producer = RabbitmqProducer(login, password, host, exchange, vhost, routing_key)
            while 1:
                news = scrapper.fetch_news_from_website()
                news_to_send = list(filter(lambda message: checker.check(message), news))
                messages = list(map(lambda message: self.create_message(message), news_to_send))
                for msg in messages:
                    response = producer.send_message(msg)
                    if response:
                        checker.mark(msg['message'])
                time.sleep(sleep_time_in_seconds)
        except Exception as e:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def create_message(message):
        return {'uuid': str(uuid.uuid1()), 'type': FEED_TYPE, 'message': message}

    @staticmethod
    def read_config_file(profile):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        if profile not in config:
            raise RuntimeError("Profile: " + profile + " not available in config file")
        host = config[profile][RABBIT_HOST]
        login = config[profile][RABBIT_LOGIN]
        password = config[profile][RABBIT_PASSWORD]
        exchange = config[profile][RABBIT_EXCHANGE]
        vhost = config[profile][RABBIT_VHOST]
        routing_key = config[profile][RABBIT_ROUTING_KEY]
        sleep_time_in_seconds = config[profile][SLEEP_TIME_IN_SECONDS]
        return host, login, password, exchange, vhost, routing_key, sleep_time_in_seconds


x = App()
x.main()
