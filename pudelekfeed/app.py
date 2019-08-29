from pudlas.pudelekfeed.scrapper.scrapper import Scrapper
from pudlas.pudelekfeed.checker.inmemory_checker import InMemoryChecker
from pudlas.pudelekfeed.rabbitmq_producer.rabbitmq_producer import RabbitmqProducer
import uuid
import json

scrapper = Scrapper()
checker = InMemoryChecker()
producer = RabbitmqProducer('admin', 'admin', 'localhost', '', 'PUDELEK', 'pudelek-feed')

# tu sie wrzuci petle
entries = scrapper.fetch_list_of_entries()

for entry in entries:
    if checker.check(entry) == True:
        checker.mark(entry)
        entry = {'uuid': str(uuid.uuid1()), 'type': 'Pudelek', 'message': entry}
        entry = json.dumps(entry, ensure_ascii=False)
        producer.send_message(entry)

    else:
        pass
    # tu waita sie wrzuci
    # tu koniec petli
producer.connection_close() #z tym nie wiem co w petli zrobic - bo jakos w koncu trzeba bedzie zamknac to polaczenie