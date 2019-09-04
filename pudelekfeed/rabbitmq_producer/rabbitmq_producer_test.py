import unittest

from .rabbitmq_producer import *


class RabbitmqProducerTest(unittest.TestCase):
    def setUp(self):
        self.producer = RabbitmqProducer('admin', 'admin', 'localhost', '', 'PUDELEK', 'pudelek-feed')

    def test_message_sending(self):
        self.assertTrue(self.producer.send_message({'message': 'test_message'}))


if __name__ == '__main__':
    unittest.main()
