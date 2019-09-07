package rabbitmqproducer

import (
	"../scraper"
	"encoding/json"
	"fmt"
	"github.com/google/uuid"
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
}

func New(login string, password string, host string, exchange string, virtualHost string, routingKey string) Producer {
	url := buildAMPQUrl(login, password, host, virtualHost)
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
	}
}

func (r RabbitmqProducer) SendMessage(news scraper.News) bool {
	message := createFeedMessage(news)
	body, err := json.Marshal(message)
	if err != nil {
		panic(err)
	}
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
