import json
import sys
import time
import traceback
import uuid

from pudelekfeed import logger
from pudelekfeed.checker.inmemory_checker import *
from pudelekfeed.rabbitmq_producer.rabbitmq_producer import *
from pudelekfeed.scrapper.scrapper import *


class App:
    def __init__(self):
        self.sleeptime = 5

    def main(self):
        try:
            scrapper = Scrapper('https://www.pudelek.pl')
            checker = InMemoryChecker()
            producer = RabbitmqProducer('admin', 'admin', 'localhost', '', 'PUDELEK', 'pudelek-feed')
            while 1:
                entries = scrapper.fetch_messages_from_pudelek()
                messages_to_send = list(filter(lambda message: checker.check(message), entries))
                messages_with_uuid = list(map(lambda message: self.add_message_uuid_and_type(message, 'Pudelek'), messages_to_send))
                messages_to_mark = list(filter(lambda message: producer.send_message(message), messages_with_uuid))
                marked_messages = list(map(lambda message: checker.mark(message), messages_to_mark))
                #for entry in entries:
                   # if checker.check(entry):
                        #checker.mark(entry)
                       # body = json.dumps({'uuid': str(uuid.uuid1()), 'type': 'Pudelek', 'message': entry}, ensure_ascii=False)
                       # body = json.dumps(entry, ensure_ascii=False)
                       # producer.send_message(body)
                        #checker.mark(entry)
                time.sleep(self.sleeptime)
        except:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)

    def add_message_uuid_and_type(self, message, type):
        modified_message = {'uuid': str(uuid.uuid1()), 'type': type}
        modified_message.update(message)
        return json.dumps(modified_message, ensure_ascii=False)


x = App()
x.main()
