package rabbitmqproducer

import (
	"../logging"
	"../scraper"
	"encoding/json"
	"fmt"
	"github.com/google/uuid"
	"github.com/sirupsen/logrus"
	"github.com/streadway/amqp"
)

const RabbitmqPort = "5672"
const Type = "SE"

type feedMessage struct {
	Uuid    string       `json:"uuid"`
	Type    string       `json:"type"`
	Message scraper.News `json:"message"`
}

type Producer interface {
	SendMessage(news scraper.News) bool
}

type RabbitmqProducer struct {
	login       string
	password    string
	host        string
	exchange    string
	virtualHost string
	routingKey  string
	connection  *amqp.Connection
	channel     *amqp.Channel
	log         *logrus.Logger
}

func New(login string, password string, host string, exchange string, virtualHost string, routingKey string) Producer {
	url := buildAMPQUrl(login, password, host, virtualHost)
	log := logging.CreateLogger()
	connection, err := amqp.Dial(url)
	if err != nil {
		panic(err)
	}
	channel, err := connection.Channel()
	if err != nil {
		panic(err)
	}
	return RabbitmqProducer{
		login:       login,
		password:    password,
		host:        host,
		exchange:    exchange,
		virtualHost: virtualHost,
		routingKey:  routingKey,
		connection:  connection,
		channel:     channel,
		log:         log,
	}
}

func (r RabbitmqProducer) SendMessage(news scraper.News) bool {
	message := createFeedMessage(news)
	body, err := json.Marshal(message)
	if err != nil {
		r.log.Error("Couldn't convert message to json: " + err.Error())
		panic(err)
	}
	r.log.Info("Sending message: " + string(body))
	response := r.channel.Publish(
		r.exchange,
		r.routingKey,
		false,
		false,
		amqp.Publishing{
			ContentType: "application/json",
			Body:        body,
		})
	if response != nil {
		r.log.Error("Got exception when sending message to rabbitmq: " + response.Error())
		panic(response)
	}
	return true
}

func createFeedMessage(news scraper.News) feedMessage {
	uuidString := uuid.New().String()
	return feedMessage{
		Uuid:    uuidString,
		Type:    Type,
		Message: news,
	}
}

func buildAMPQUrl(login string, password string, host string, virtualHost string) string {
	return fmt.Sprintf("amqp://"+"%s:%s"+"@"+"%s"+":"+RabbitmqPort+"/"+"%s", login, password, host, virtualHost)
}
