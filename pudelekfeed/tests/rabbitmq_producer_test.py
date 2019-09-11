import unittest

from pudelekfeed.rabbitmq_producer.rabbitmq_producer import *


class RabbitmqProducerTest(unittest.TestCase):
    def setUp(self):
        self.producer = RabbitmqProducer('admin', 'admin', 'localhost', '', 'PUDELEK', 'pudelek-feed')
        self.message = {'id': '150762',
                        'date': '2019-09-09 13:00:00',
                        'title': 'Edyta Górniak zaśpiewa na otwarciu nowego "Big Brothera". Też nie możecie się doczekać?',
                        'description': 'Piosenkarka sprawdza się w roli "twarzy" stacji. Została ulubienicą Edwarda Miszczaka?',
                        'tags': ['Edyta Górniak', 'Big Brother'],
                        'link': 'https://www.pudelek.pl/artykul/150762/edyta_gorniak_zaspiewa_na_otwarciu_nowego_big_brothera_tez_nie_mozecie_sie_doczekac/'}

    def test_send_message_should_return_true_if_message_has_been_sent_successfully(self):
        self.assertTrue(self.producer.send_message(self.message))


if __name__ == '__main__':
    unittest.main()

