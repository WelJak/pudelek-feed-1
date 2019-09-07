from pudelekfeed import logger
from .checker import Checker


class InMemoryChecker(Checker):
    def __init__(self):
        self.entries = []

    def check(self, entry):
        if entry in self.entries:
            logger.info('message: {} has been already sent'.format(entry))
            return False
        else:
            logger.info('message: {} has not been sent yet'.format(entry))
            return True

    def mark(self, entry):
        self.entries.append(entry)
        logger.info('message: {} has been marked as sent'.format(entry))
