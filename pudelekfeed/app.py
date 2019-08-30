import json
import sys
import time
import traceback
import uuid

from pudlas.pudelekfeed import logger
from pudlas.pudelekfeed.checker.inmemory_checker import InMemoryChecker
from pudlas.pudelekfeed.rabbitmq_producer.rabbitmq_producer import RabbitmqProducer
from pudlas.pudelekfeed.scrapper.scrapper import Scrapper


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
                #messages_sent = list(map(lambda message: producer.send_message(message), messages_with_uuid))
                messages_to_mark = list(filter(lambda message: producer.send_message(message), messages_with_uuid))
                marked_messages = list(map(lambda message: checker.mark(message), messages_to_mark))
                #for entry in entries:
                   #if checker.check(entry):
                       #checker.mark(entry)
                       #entry = {'uuid': str(uuid.uuid1()), 'type': 'Pudelek', 'message': entry}
                       #entry = json.dumps(entry, ensure_ascii=False)
                       #producer.send_message(entry)

                   # else:
                    #    logger.info('Message with uuid: {} is marked as sent'.format(entry['uuid']))

                time.sleep(self.sleeptime)

        except:
            logger.info('An error occurred during process:')
            traceback.print_exc(file=sys.stdout)

    def add_message_uuid_and_type(self,message, type):
        modified_message = {'uuid': str(uuid.uuid1()), 'type': type, 'message': message}
        return json.dumps(modified_message, ensure_ascii=False)

x = App()
x.main()