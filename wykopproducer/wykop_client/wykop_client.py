import hashlib
import json
import sys
import traceback

import logger

WYKOP_ADD_ENTRY_URL = 'https://a2.wykop.pl/Entries/Entry/entry/'
WYKOP_ADD_LINK_URL = 'https://a2.wykop.pl/Addlink/Add/'
WYKOP_LINK_DRAFT_URL = 'https://a2.wykop.pl/Addlink/Draft/'


class WykopClient:
    def __init__(self, appkey, secret_key, user_key):
        self.WYKOP_APP_KEY = appkey
        self.WYKOP_SECRET_KEY = secret_key
        self.WYKOP_USER_KEY = user_key

    def prepare_link_draft(self, message):
        link_draft_post_params = {'url': message['message']['link']}
        link_draft_headers = {
            'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                               WYKOP_LINK_DRAFT_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                               post_params=','.join(
                                                   '{}'.format(link_draft_post_params[key]) for key in
                                                   link_draft_post_params)),
            'Content-type': 'application/x-www-form-urlencoded'
        }
        wykop_link_draft_client = self.requests.post(
            self.WYKOP_SECRET_KEY,
            WYKOP_LINK_DRAFT_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=link_draft_post_params,
            headers=link_draft_headers
        )
        return json.loads(wykop_link_draft_client.json())
    def add_link(self, message, draft_response):
        key = ''  # patrz dokumentacja
        addlink_post_params = {'title': message['message']['title'],
                               'descritpion': message['message']['description'],
                               'tags': ', '.join(message['message']['tags']),
                               'photo': draft_response['data']['compact']['photos']['key'],
                               'url': message['message']['link'],
                               'plus18': True}
        addlink_headers = {
            'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                               WYKOP_ADD_LINK_URL + 'key/' + key + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                               post_params=','.join('{}'.format(addlink_post_params[key]) for key in
                                                                    addlink_post_params)),
            'Content-type': 'application/x-www-form-urlencoded'
        }
        wykop_addlink_client = self.requests.post(
            WYKOP_ADD_LINK_URL + 'key/' + key + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=addlink_post_params, headers=addlink_headers)
        return json.loads(wykop_addlink_client.json())
    def add_entry(self, addlink_response):
        addentry_post_params = {
            'body': 'Patrzcie co znalazlem ' + addlink_response['data']['compact']['full']['url'],
            'embed': '',
            'adultmedia': False
        }
        addentry_headers = {
            'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                               WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                               post_params=','.join(
                                                   '{}'.format(addentry_post_params[key]) for key in
                                                   addentry_post_params)),
            'Content-type': 'application/x-www-form-urlencoded'
        }
        wykop_entry_client = self.requests.post(
            WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=addentry_post_params,
            headers=addentry_headers)
        if wykop_entry_client.status_code == 200:
            return True
        else:
            return False, logger.info('Message has not been sent to wykop.pl')


    @staticmethod
    def create_md5checksum(secret, url, post_params=''):
        value_to_count = secret + url + post_params
        return hashlib.md5(value_to_count.encode('utf-8')).hexdigest()
