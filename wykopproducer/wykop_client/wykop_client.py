import hashlib

import requests

WYKOP_ADD_ENTRY_URL = 'https://a2.wykop.pl/Entries/Entry/entry/'
WYKOP_ADD_LINK_URL = 'https://a2.wykop.pl/Addlink/Add/'
WYKOP_LINK_DRAFT_URL = 'https://a2.wykop.pl/Addlink/Draft/'
WYKOP_LOG_IN_URL = 'https://a2.wykop.pl/Login/Index/'
WYKOP_PREPARE_THUMBNAIL_URL = 'https://a2.wykop.pl/Addlink/Images/'


class WykopClient:
    def __init__(self, appkey, secret_key, login, account_key):
        self.WYKOP_APP_KEY = appkey
        self.WYKOP_SECRET_KEY = secret_key
        self.WYKOP_USER_KEY = ''
        self.WYKOP_USER_LOGIN = login
        self.WYKOP_ACCOUNT_KEY = account_key

    def log_in(self):
        log_in_postparams = {'login': self.WYKOP_USER_LOGIN,
                             'accountkey': self.WYKOP_ACCOUNT_KEY}
        log_in_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                             WYKOP_LOG_IN_URL + 'appkey/' + self.WYKOP_APP_KEY + '/accountkey/' + self.WYKOP_ACCOUNT_KEY,
                                                             post_params=','.join(
                                                                 '{}'.format(log_in_postparams[key]) for key in
                                                                 log_in_postparams))}
        response = requests.post(
            url=WYKOP_LOG_IN_URL + 'appkey/' + self.WYKOP_APP_KEY + '/accountkey/' + self.WYKOP_ACCOUNT_KEY,
            data=log_in_postparams,
            headers=log_in_headers)
        return response.json()['data']['userkey']

    def prepare_link_for_posting(self, message):
        prepare_link_post_params = {'url': message['message']['link']}
        prepare_link_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                                   WYKOP_LINK_DRAFT_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                                                   prepare_link_post_params['url'])}
        response = requests.post(
            WYKOP_LINK_DRAFT_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=prepare_link_post_params,
            headers=prepare_link_headers)
        return response.json()

    def prepare_news_thumbnail(self, prepare_link_response):
        prepare_thumbnail_nameparam = prepare_link_response['data']['key']
        prepare_thumbnail_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                                        WYKOP_PREPARE_THUMBNAIL_URL + 'key/' + prepare_thumbnail_nameparam + '/appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY)}
        response = requests.post(
            WYKOP_PREPARE_THUMBNAIL_URL + 'key/' + prepare_thumbnail_nameparam + '/appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            headers=prepare_thumbnail_headers)
        return response.json()

    def add_link_on_wykop(self, prepare_link_response, prepare_thumbnail_response, message):
        add_link_nameparam = prepare_link_response['data']['key']
        add_link_postparams = {'title': prepare_link_response['data']['title'],
                               'description': message['message']['description'],
                               'tags': ','.join(message['message']['tags']).replace(' ', ''),
                               'photo': prepare_thumbnail_response['data'][0]['key'],
                               'url': message['message']['link']}
        add_link_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                               WYKOP_ADD_LINK_URL + 'key/' + add_link_nameparam + '/appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                                               post_params=','.join(
                                                                   '{}'.format(add_link_postparams[key]) for key in
                                                                   add_link_postparams))}
        response = requests.post(
            WYKOP_ADD_LINK_URL + 'key/' + add_link_nameparam + '/appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=add_link_postparams,
            headers=add_link_headers)
        return response.json()

    def add_entry(self, addlink_response):
        add_entry_postparams = {
            'body': 'Sprawdź to https://www.wykop.pl/link/{}'.format(addlink_response['data']['id']),
            'adultmedia': False}
        add_entry_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                                WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
                                                                post_params=','.join(
                                                                    '{}'.format(add_entry_postparams[key]) for key in
                                                                    add_entry_postparams)),
                             'Content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + self.WYKOP_USER_KEY,
            data=add_entry_postparams, headers=add_entry_headers)
        if response.json()['data']['id']:
            return True

    @staticmethod
    def create_md5checksum(secret, url, post_params=''):
        value_to_count = secret + url + post_params
        return hashlib.md5(value_to_count.encode('utf-8')).hexdigest()


class WykopClientMock:
    def __init__(self, *args, **kwargs):
        pass

    def log_in(self):
        return 'mocmock'

    def prepare_link_for_posting(self, *args, **kwargs):
        return {'data': {'compact': {'photos': {'key': 'photokey'}}}}

    def prepare_news_thumbnail(self, *args, **kwargs):
        return 'mockmock'

    def add_link_on_wykop(self, *args, **kwargs):
        return {'data': {'compact': {'full': {'url': 'www.url.url'}}}}

    def add_entry(self, *args, **kwargs):
        return True
