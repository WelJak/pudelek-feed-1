import json

import requests

import logger

API_CHECK_MESSAGE_URL = 'http://localhost:8080/check'
API_MARK_MESSAGE_URL = 'http://localhost:8080/messages'


class ApiClient:
    def checkIfMessageWasSent(self, message):
        check_message_postparams = json.dumps({
            'uuid': message['uuid'],
            'type': message['type'],
            'entryid': message['message']['id'],
            'post_date': message['message']['date'],
            'title': message['message']['title'],
            'description': message['message']['description'],
            'tags': message['message']['tags'],
            'link': message['message']['link']
        })

        check_message_headers = {
            'Content-type': 'application/json'
        }
        response = requests.post(
            API_CHECK_MESSAGE_URL,
            data=check_message_postparams,
            headers=check_message_headers
        )
        if response.json()['issent']:
            logger.info('message {} has been already sent'.format(message['message']['id']))
            return False
        else:
            logger.info('message {} has not been sent yet'.format(message['message']['id']))
            return True

    def checkIfMessageWasSentToWykop(self, entryid):
        check_message_details_params = {
            'Content-type': 'application/json'
        }
        response = requests.get(API_MARK_MESSAGE_URL + '/' + entryid)
        if not response.json()['wassent']:
            return True
        else:
            return False

    def markMessage(self, message):
        mark_message_headers = {
            'Content-type': 'application/json'
        }
        response = requests.get(
            API_MARK_MESSAGE_URL + '/' + message['message']['id'] + '/mark',
            headers=mark_message_headers
        )

        if response.json()['sentSuccessfully']:
            logger.info('message {} has been successfully marked'.format(message['message']['id']))
            return True
        else:
            logger.info('message {} has not been marked'.format(message['message']['id']))
            return False
