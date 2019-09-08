package main

import (
	"../../internal/checker"
	"../../internal/configloader"
	"../../internal/rabbitmqproducer"
	"../../internal/scraper"
	"fmt"
)

const envConfigPath = "configs/"

func main() {
	environment := configloader.Getenv("ENVIRONMENT", "LOCAL")
	fmt.Println("ENV: " + environment)
	config := configloader.Load(environment)
	websiteScraper := scraper.New(configloader.WebsiteUrl)
	newsChecker := checker.New()
	messageProducer := rabbitmqproducer.New(config.RabbitLogin, config.RabbitPassword, config.RabbitHost, config.RabbitExchange, config.RabbitVhost, config.RabbitRoutingKey)
	news := websiteScraper.FetchNewsFromWebsite()
	newsToSend := scraper.Filter(news, func(n scraper.News) bool {
		return newsChecker.Check(n)
	})
	for _, n := range newsToSend {
		response := messageProducer.SendMessage(n)
		if response {
			newsChecker.Mark(n)
		}
	}
}
