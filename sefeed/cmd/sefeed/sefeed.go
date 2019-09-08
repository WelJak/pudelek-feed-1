package main

import (
	"../../internal/checker"
	"../../internal/configloader"
	"../../internal/logging"
	"../../internal/rabbitmqproducer"
	"../../internal/scraper"
)

func main() {
	environment := configloader.Getenv("ENVIRONMENT", "LOCAL")
	log := logging.InitLoggerFactory(environment).CreateLogger()
	log.Info("Running sefeed with environment: ", environment)
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
