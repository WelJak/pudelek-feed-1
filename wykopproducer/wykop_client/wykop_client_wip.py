import hashlib

import requests

WYKOP_ADD_ENTRY_URL = 'https://a2.wykop.pl/Entries/Add/'
WYKOP_ADD_LINK_URL = 'https://a2.wykop.pl/Addlink/Add/'
WYKOP_LINK_DRAFT_URL = 'https://a2.wykop.pl/Addlink/Draft/'
WYKOP_LOG_IN_URL = 'https://a2.wykop.pl/Login/Index/'


class WykopClient:
    def __init__(self, appkey, secret_key, user_key, login, account_key):
        self.WYKOP_APP_KEY = appkey
        self.WYKOP_SECRET_KEY = secret_key
        # self.WYKOP_USER_KEY = user_key
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

    def prepare_link_draft(self):
        pass

    def add_link(self):
        pass

    def add_entry(self, userkey):
        add_entry_postparams = {'body': 'test123 api wykop',
                                'adultmedia': False}
        add_entry_headers = {'apisign': self.create_md5checksum(self.WYKOP_SECRET_KEY,
                                                                WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + userkey,
                                                                post_params=','.join(
                                                                    '{}'.format(add_entry_postparams[key]) for key in
                                                                    add_entry_postparams)),
                             'Content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(WYKOP_ADD_ENTRY_URL + 'appkey/' + self.WYKOP_APP_KEY + '/userkey/' + userkey,
                                 data=add_entry_postparams, headers=add_entry_headers)
        if response.json()['data']['id']:
            return True

    @staticmethod
    def create_md5checksum(secret, url, post_params=''):
        value_to_count = secret + url + post_params
        return hashlib.md5(value_to_count.encode('utf-8')).hexdigest()
