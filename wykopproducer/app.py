import configparser
import os

from wykopproducer.checker.checker import *
from wykopproducer.rabbitmq_listener.rabbitmq_listener import *
from wykopproducer.wykop_client.wykop_client import *

RABBIT_HOST = 'RABBIT_HOST'
RABBIT_LOGIN = 'RABBIT_LOGIN'
RABBIT_PASSWORD = 'RABBIT_PASSWORD'
RABBIT_EXCHANGE = 'RABBIT_EXCHANGE'
RABBIT_VHOST = 'RABBIT_VHOST'
RABBIT_QUEUE = 'RABBIT_QUEUE'
CONFIG_FILE = "variables.ini"

DEFAULT_PROFILE = "LOCAL"

WYKOP_APP_KEY = '123'
WYKOP_SECRET_KEY = '321'
WYKOP_USER_KEY = 'abcd'


class App:
    def __init__(self):
        self.api = WykopClientMock(WYKOP_APP_KEY, WYKOP_SECRET_KEY, WYKOP_USER_KEY)
        self.checker = Checker()

    def publish_news(self, message):
        if self.checker.check(message['message']):
            message_to_send = message['message']
        draft_link_response = self.api.prepare_link_draft(message_to_send)
        add_link_response = self.api.add_link(draft_link_response)
        add_entry_response = self.api.add_entry(add_link_response)
        if add_entry_response:
            logger.info('message {} has been successfully sent to wykop.pl'.format(message_to_send))
            self.checker.mark(message_to_send)

    def main(self):
        profile = os.getenv('ENVIRONMENT', DEFAULT_PROFILE)
        logger.info("Running wykop client with active profile: " + profile)
        host, login, password, exchange, vhost, queue = self.read_config_file(profile)
        try:
            rabbitListener = RabbitmqListener(login, password, host, exchange, vhost, queue)
            rabbitListener.listen(self.publish_news)
        except Exception as e:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)
            raise e

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
        queue = config[profile][RABBIT_QUEUE]
        return host, login, password, exchange, vhost, queue


x = App()
x.main()
