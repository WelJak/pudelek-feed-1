import configparser
# import requests
import hashlib
import os
from unittest import mock

from wykopproducer.rabbitmq_listener.rabbitmq_listener import *

RABBIT_HOST = 'RABBIT_HOST'
RABBIT_LOGIN = 'RABBIT_LOGIN'
RABBIT_PASSWORD = 'RABBIT_PASSWORD'
RABBIT_EXCHANGE = 'RABBIT_EXCHANGE'
RABBIT_VHOST = 'RABBIT_VHOST'
RABBIT_QUEUE = 'RABBIT_QUEUE'
CONFIG_FILE = "variables.ini"

DEFAULT_PROFILE = "LOCAL"

mock = mock.Mock()
WYKOP_APP_KEY = '123'
WYKOP_SECRET_KEY = '321'
WYKOP_ADD_ENTRY_URL = 'https://a2.wykop.pl/Entries/Entry/entry/'


class App:
    def client(self, message):
        self.requests = mock
        try:
            headers = {
                'apisign': self.create_md5checksum(WYKOP_SECRET_KEY, WYKOP_ADD_ENTRY_URL + 'appkey/' + WYKOP_APP_KEY),
                'Content-type': 'application/x-www-form-urlencoded'}
            post_params = {'body': message, 'embed': '', 'adultmedia': False}
            wykop_client = self.requests.post(WYKOP_ADD_ENTRY_URL + 'appkey/' + WYKOP_APP_KEY, data=post_params,
                                              headers=headers)
            if wykop_client.status_code == 200:
                logger.info('Added new entry on wykop.pl')
            elif wykop_client.status_code == 404:
                logger.info('Response code 404 - posting new entry was unsuccessful')
        except:
            logger.info('An error occurred during sending message to wykop.pl')
            traceback.print_exc(file=sys.stdout)

    def main(self):
        profile = os.getenv('ENVIRONMENT', DEFAULT_PROFILE)
        logger.info("Running wykop client with active profile: " + profile)
        host, login, password, exchange, vhost, queue = self.read_config_file(profile)
        try:
            rabbitListener = RabbitmqListener(login, password, host, exchange, vhost, queue)
            rabbitListener.listen(self.client)
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

    @staticmethod
    def create_md5checksum(secret, url, post_params=''):
        value_to_count = secret + url + post_params
        return hashlib.md5(value_to_count.encode('utf-8')).hexdigest()


x = App()
x.main()
