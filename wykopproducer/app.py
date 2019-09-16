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
WYKOP_USER_KEY = 'abcd'
WYKOP_ADD_ENTRY_URL = 'https://a2.wykop.pl/Entries/Entry/entry/'
WYKOP_ADD_LINK_URL = 'https://a2.wykop.pl/Addlink/Add/'
WYKOP_LINK_DRAFT_URL = 'https://a2.wykop.pl/Addlink/Draft/'


class App:
    def client(self, message):
        self.requests = mock
        json = mock
        try:
            link_draft_headers = {
                'apisign': self.create_md5checksum(WYKOP_SECRET_KEY, WYKOP_LINK_DRAFT_URL+'appkey/'+WYKOP_APP_KEY+'/userkey/'+WYKOP_USER_KEY),
                'Content-type': 'application/x-www-form-urlencoded'
            }
            link_draft_post_params = {'url': message['message']['link']}
            wykop_link_draft_client = self.requests.post(
                WYKOP_SECRET_KEY, WYKOP_LINK_DRAFT_URL + 'appkey/' + WYKOP_APP_KEY + '/userkey/' + WYKOP_USER_KEY,
                data=link_draft_post_params,
                headers=link_draft_headers
            )
            draft_response = json.loads(wykop_link_draft_client.json())

            key = ''  # patrz dokumentacja
            addlink_headers = {
                'apisign': self.create_md5checksum(WYKOP_SECRET_KEY,
                                                   WYKOP_ADD_LINK_URL + 'key/' + key + 'appkey/' + WYKOP_APP_KEY + '/userkey/' + WYKOP_USER_KEY),
                'Content-type': 'application/x-www-form-urlencoded'
            }
            addlink_post_params = {'title': message['message']['title'],
                                   'descritpion': message['message']['description'],
                                   'tags': ', '.join(['message']['tags']),
                                   'photo': draft_response['data']['compact']['photos']['key'],
                                   'url': message['message']['link'],
                                   'plus18': True}
            wykop_addlink_client = self.requests.post(
                WYKOP_ADD_LINK_URL + 'key/' + key + 'appkey/' + WYKOP_APP_KEY + '/userkey/' + WYKOP_USER_KEY,
                data=addlink_post_params, headers=addlink_headers)
            wykop_addlink_respone = json.loads(wykop_addlink_client.json())

            addentry_headers = {
                'apisign': self.create_md5checksum(WYKOP_SECRET_KEY,
                                                   WYKOP_ADD_ENTRY_URL + 'appkey/' + WYKOP_APP_KEY + '/userkey/' + WYKOP_USER_KEY),
                'Content-type': 'application/x-www-form-urlencoded'}
            addentry_post_params = {'body': 'Patrzcie co znalazlem '+ wykop_addlink_respone['data']['compact']['full']['url'], 'embed': '', 'adultmedia': False}
            wykop_entry_client = self.requests.post(
                WYKOP_ADD_ENTRY_URL + 'appkey/' + WYKOP_APP_KEY + '/userkey/' + WYKOP_USER_KEY,
                data=addentry_post_params,
                headers=addentry_headers)
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
