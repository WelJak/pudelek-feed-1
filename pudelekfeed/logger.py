import logging
import os
import sys

log_level_dictionary = {"LIVE": logging.INFO, "DEV": logging.INFO, "LOCAL": logging.DEBUG}

environment = os.getenv('ENVIRONMENT')

log_level = log_level_dictionary.get(environment, logging.DEBUG)
log = logging.getLogger()
log.setLevel(log_level)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


def info(message):
    log.info(message)


def debug(message):
    log.debug(message)


def warning(message):
    log.warning(message)
