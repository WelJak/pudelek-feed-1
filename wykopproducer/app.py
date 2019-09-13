import configparser
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

FEED_TYPE = 'PUDELEK'
WEBSITE_URL = 'https://www.pudelek.pl'
DEFAULT_PROFILE = "LOCAL"

mock = mock.Mock()


class App:
    def logic(self, message):
        self.wykopInterface = mock
        try:
            # tu jakas logika ktora rozbije ten dict na odpowiednie czesci a potem powsadza w odpowiednie funkcje przy uzyciu api - to popatrzec dokumentacje musze
            self.wykopInterface.send_news_to_wykop(message)
            self.wykopInterface.send_news_to_wykop.return_value = logger.info(
                'Message {} has been successfully sent to wykop.pl'.format(message))
        except:
            logger.info('An error occurred during sending message to wykop.pl')
            traceback.print_exc(file=sys.stdout)

    def main(self):
        profile = os.getenv('ENVIRONMENT', DEFAULT_PROFILE)
        logger.info("Running pudelek feed with active profile: " + profile)
        host, login, password, exchange, vhost, queue = self.read_config_file(profile)
        try:
            rabbitListener = RabbitmqListener(login, password, host, exchange, vhost, queue)
            rabbitListener.listen(self.logic)
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
