# pudelek-feed

### Opis projektu
Aplikacja monitoruje stronę główną pudelka - za każdym razem kiedy pojawi się nowa wiadomość zostanie ona wrzucona jako znalezisko na wykop.pl z wpisem na mikroblogu zachęcającym o wykopywania. Jednocześnie do aplikacji dołąćzony jest dashboard przez który użytkownik może przejrzeć wszystkie dodane znaleziska, zobaczyć najpopularniejsze komentarze, pofiltrować je w zależności od różnych statystyk. Dashboard również oferuje zabezpieczony widok dla adminów pozwalający na usuwanie i sterowanie aplikacją. 

**Wykonanie projektu dzielone na 3 milestony:**
* **0.0.1** - działający program scrapujący nowe wiadomości z pudelka i wrzucający je jako znaleziska na wykop
* **0.0.2** - + przetrzymywanie wrzuconych wiadomości i prosty dashboard umożliwiwający podstawowe ich przejrzenie
* **1.0.0** - + wszystkie funkcje w dashboardzie, dashboard dla adminów 

### Architektura
Ideowe przedstawienie rozwiązania
![alt text](https://raw.githubusercontent.com/solveretur/pudelek-feed/master/architektura.jpg)

Architektura mikroserwisowa. Komunikacja odbywa się przy pomocy kolejki rabbitmq. Aplikacja składa się z 5 osobnych mikroseriwsów:
* pudelek feed - serwis ściągający najnowsze wiadomości z pudelka 
* wykop producer - serwis wrzucający znalezisko na wykop, dodający wpis na mikro
* storage service - serwis zarządzający api do storage (bazy postgresql)
* authentication service - serwis authentykujący czy jest adminem czy nie
* dahsboard - aplikacja dashboard

### Nauka
* pudelek feed - scrapowanie danych z stron www, wysyłanie wiadmości na rabbita
* kolejka - kolejki, rabbitmq, nauka dockera
* wykop producer - tworzenie klienta rest api
* storage service - nauka zapytań baz danych, postgresa, docker
* authentication service - podstawowa nauka o security
* dashboard - pisanie webapki

### Plan działania
* Sprinty tygodniowe, codzienne daily
* Progress sprawdzany przy pomocy kanban boardu: https://github.com/solveretur/pudelek-feed/projects/1
