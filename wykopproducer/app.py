import configparser
import os

from apiclient.api_client import *
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
WYKOP_APP_KEY = 'WYKOP_APP_KEY'
WYKOP_SECRET_KEY = 'WYKOP_SECRET_KEY'
WYKOP_LOGIN = 'WYKOP_LOGIN'
WYKOP_ACCOUNT_KEY = 'WYKOP_ACCOUNT_KEY'

DEFAULT_PROFILE = "LOCAL"


class App:
    def __init__(self):
        self.api = None
        self.checker = Checker()
        self.api_client = ApiClient()

    def publish_news(self, message):
        if self.api_client.checkIfMessageWasSentToWykop(message['message']['id']):
            message_to_send = message
            prepare_link_response = self.api.prepare_link_for_posting(message_to_send)
            if 'error' in prepare_link_response:
                logger.info('An error occured during preparing message: {}'.format(prepare_link_response['error']))
                self.api_client.markMessage(message_to_send)
            else:
                prepare_thumbnail_response = self.api.prepare_news_thumbnail(prepare_link_response)
                add_link_response = self.api.add_link_on_wykop(prepare_link_response,
                                                               prepare_thumbnail_response,
                                                               message_to_send)
                if 'error' in add_link_response:
                    logger.info(
                        'An error ocured during posting message on wykop: {}'.format(add_link_response['error']))
                else:
                    add_entry_response = self.api.add_entry(add_link_response)
                    if add_entry_response:
                        logger.info(
                            'message {} has been successfully sent to wykop.pl'.format(message_to_send['message']))
                        self.api_client.markMessage(message_to_send)
        else:
            logger.info('message {} has been already sent to wykop'.format(message['message']['id']))

    def main(self):
        profile = os.getenv('ENVIRONMENT', DEFAULT_PROFILE)
        logger.info("Running wykop client with active profile: " + profile)
        host, login, password, exchange, vhost, queue, appkey, secret, wykoplogin, acckey = self.read_config_file(
            profile)
        if profile == 'LOCAL':
            self.api = WykopClientMock(appkey, secret, wykoplogin, acckey)
            self.api.WYKOP_USER_KEY = self.api.log_in()
        elif profile == 'DEV':
            self.api = WykopClientMock(appkey, secret, wykoplogin, acckey)
            self.api.WYKOP_USER_KEY = self.api.log_in()
        else:
            self.api = WykopClient(appkey, secret, wykoplogin, acckey)
            self.api.WYKOP_USER_KEY = self.api.log_in()
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
        appkey = config[profile][WYKOP_APP_KEY]
        secret = config[profile][WYKOP_SECRET_KEY]
        wykoplogin = config[profile][WYKOP_LOGIN]
        acckey = config[profile][WYKOP_ACCOUNT_KEY]
        return host, login, password, exchange, vhost, queue, appkey, secret, wykoplogin, acckey


x = App()
x.main()
