import json

import requests
import logger
API_CHECK_MESSAGE_URL = 'http://localhost:8080/check'


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
