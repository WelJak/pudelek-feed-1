from pudlas.pudelekfeed.scrapper.scrapper import Scrapper
from pudlas.pudelekfeed.checker.inmemory_checker import InMemoryChecker
from pudlas.pudelekfeed.rabbitmq_producer.rabbitmq_producer import RabbitmqProducer
import uuid
import json
import time
import sys
import traceback
from pudlas.pudelekfeed import logger

try:
    scrapper = Scrapper()
    checker = InMemoryChecker()
    producer = RabbitmqProducer('admin', 'admin', 'localhost', '', 'PUDELEK', 'pudelek-feed')
    sleeptime = 120
    while 1:
        entries = scrapper.fetch_list_of_entries()

        for entry in entries:
            if checker.check(entry) == True:
                checker.mark(entry)
                entry = {'uuid': str(uuid.uuid1()), 'type': 'Pudelek', 'message': entry}
                entry = json.dumps(entry, ensure_ascii=False)
                producer.send_message(entry)

            else:
                pass
               # logger.info('Message wit uuid: {} is marked as sent'.format(entry['uuid']))

        time.sleep(sleeptime)

except:
    logger.info('An error occurred during process:')
    traceback.print_exc(file=sys.stdout)
