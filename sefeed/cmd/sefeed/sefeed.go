package main

import (
	"../../internal/checker"
	"../../internal/rabbitmqproducer"
	"../../internal/scraper"
)

const WebsiteUrl = "https://se.pl"

func main() {
	websiteScraper := scraper.New(WebsiteUrl)
	newsChecker := checker.New()
	messageProducer := rabbitmqproducer.New("admin", "admin", "localhost", "feed-exchange", "PUDELEK", "PUDELEK")
	news := websiteScraper.FetchNewsFromWebsite()
	newsToSend := filter(news, func(n scraper.News) bool {
		return newsChecker.Check(n)
	})
	for _, n := range newsToSend {
		response := messageProducer.SendMessage(n)
		if response {
			newsChecker.Mark(n)
		}
	}
}

func filter(vs []scraper.News, f func(scraper.News) bool) []scraper.News {
	vsf := make([]scraper.News, 0)
	for _, v := range vs {
		if f(v) {
			vsf = append(vsf, v)
		}
	}
	return vsf
}
