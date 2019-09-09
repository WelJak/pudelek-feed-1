import unittest

from pudelekfeed.checker.inmemory_checker import *


class InMemoryCheckerTest(unittest.TestCase):
    def setUp(self):
        self.x = InMemoryChecker()
        self.x.entries = [{'id': '150762',
                           'date': '2019-09-09 13:00:00',
                           'title': 'Edyta Górniak zaśpiewa na otwarciu nowego "Big Brothera". Też nie możecie się doczekać?',
                           'description': 'Piosenkarka sprawdza się w roli "twarzy" stacji. Została ulubienicą Edwarda Miszczaka?',
                           'tags': ['Edyta Górniak', 'Big Brother'],
                           'link': 'https://www.pudelek.pl/artykul/150762/edyta_gorniak_zaspiewa_na_otwarciu_nowego_big_brothera_tez_nie_mozecie_sie_doczekac/'}]

    def test_check_should_return_True_when_message_has_not_been_sent(self):
        self.assertTrue(self.x.check({'id': '150760',
                                      'date': '2019-09-09 12:30:00',
                                      'title': 'Aktor serialu "Na dobre i na złe" znów narzeka na brak pracy. "Reżyser zdecydował, że zagra inny aktor"',
                                      'description': 'Mało znany aktor, mąż znanej aktorki, niedawno miał stracić rolę w serialu przez homofobiczne wpisy na Twitterze. "W Polsce reżyser jest widocznie ponad prawem" - skarży się Klynstra. ',
                                      'tags': ['Redbad Klynsta'],
                                      'link': 'https://www.pudelek.pl/artykul/150760/aktor_serialu_na_dobre_i_na_zle_znow_narzeka_na_brak_pracy_rezyser_zdecydowal_ze_zagra_inny_aktor/'}))

    def test_check_should_return_False_when_message_has_been_sent(self):
        self.assertFalse(self.x.check({'id': '150762',
                                       'date': '2019-09-09 13:00:00',
                                       'title': 'Edyta Górniak zaśpiewa na otwarciu nowego "Big Brothera". Też nie możecie się doczekać?',
                                       'description': 'Piosenkarka sprawdza się w roli "twarzy" stacji. Została ulubienicą Edwarda Miszczaka?',
                                       'tags': ['Edyta Górniak', 'Big Brother'],
                                       'link': 'https://www.pudelek.pl/artykul/150762/edyta_gorniak_zaspiewa_na_otwarciu_nowego_big_brothera_tez_nie_mozecie_sie_doczekac/'}))

    def test_mark_should_add_new_message_to_list_of_sent_messages_then_check_should_return_False(self):
        self.x.mark({'id': '150760',
                     'date': '2019-09-09 12:30:00',
                     'title': 'Aktor serialu "Na dobre i na złe" znów narzeka na brak pracy. "Reżyser zdecydował, że zagra inny aktor"',
                     'description': 'Mało znany aktor, mąż znanej aktorki, niedawno miał stracić rolę w serialu przez homofobiczne wpisy na Twitterze. "W Polsce reżyser jest widocznie ponad prawem" - skarży się Klynstra. ',
                     'tags': ['Redbad Klynsta'],
                     'link': 'https://www.pudelek.pl/artykul/150760/aktor_serialu_na_dobre_i_na_zle_znow_narzeka_na_brak_pracy_rezyser_zdecydowal_ze_zagra_inny_aktor/'})
        self.assertFalse(self.x.check({'id': '150760',
                                       'date': '2019-09-09 12:30:00',
                                       'title': 'Aktor serialu "Na dobre i na złe" znów narzeka na brak pracy. "Reżyser zdecydował, że zagra inny aktor"',
                                       'description': 'Mało znany aktor, mąż znanej aktorki, niedawno miał stracić rolę w serialu przez homofobiczne wpisy na Twitterze. "W Polsce reżyser jest widocznie ponad prawem" - skarży się Klynstra. ',
                                       'tags': ['Redbad Klynsta'],
                                       'link': 'https://www.pudelek.pl/artykul/150760/aktor_serialu_na_dobre_i_na_zle_znow_narzeka_na_brak_pracy_rezyser_zdecydowal_ze_zagra_inny_aktor/'}))

    def test_mark_should_add_new_message_to_list_of_sent_messages_then_the_list_should_contain_two_messages(self):
        self.x.mark({'id': '150760',
                     'date': '2019-09-09 12:30:00',
                     'title': 'Aktor serialu "Na dobre i na złe" znów narzeka na brak pracy. "Reżyser zdecydował, że zagra inny aktor"',
                     'description': 'Mało znany aktor, mąż znanej aktorki, niedawno miał stracić rolę w serialu przez homofobiczne wpisy na Twitterze. "W Polsce reżyser jest widocznie ponad prawem" - skarży się Klynstra. ',
                     'tags': ['Redbad Klynsta'],
                     'link': 'https://www.pudelek.pl/artykul/150760/aktor_serialu_na_dobre_i_na_zle_znow_narzeka_na_brak_pracy_rezyser_zdecydowal_ze_zagra_inny_aktor/'})
        self.assertEqual(self.x.entries, [{'id': '150762',
                                           'date': '2019-09-09 13:00:00',
                                           'title': 'Edyta Górniak zaśpiewa na otwarciu nowego "Big Brothera". Też nie możecie się doczekać?',
                                           'description': 'Piosenkarka sprawdza się w roli "twarzy" stacji. Została ulubienicą Edwarda Miszczaka?',
                                           'tags': ['Edyta Górniak', 'Big Brother'],
                                           'link': 'https://www.pudelek.pl/artykul/150762/edyta_gorniak_zaspiewa_na_otwarciu_nowego_big_brothera_tez_nie_mozecie_sie_doczekac/'},
                                          {'id': '150760',
                                           'date': '2019-09-09 12:30:00',
                                           'title': 'Aktor serialu "Na dobre i na złe" znów narzeka na brak pracy. "Reżyser zdecydował, że zagra inny aktor"',
                                           'description': 'Mało znany aktor, mąż znanej aktorki, niedawno miał stracić rolę w serialu przez homofobiczne wpisy na Twitterze. "W Polsce reżyser jest widocznie ponad prawem" - skarży się Klynstra. ',
                                           'tags': ['Redbad Klynsta'],
                                           'link': 'https://www.pudelek.pl/artykul/150760/aktor_serialu_na_dobre_i_na_zle_znow_narzeka_na_brak_pracy_rezyser_zdecydowal_ze_zagra_inny_aktor/'}])


if __name__ == '__main__':
    unittest.main()
