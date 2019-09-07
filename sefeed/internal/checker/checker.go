package checker

import (
	"../scraper"
	"reflect"
)

type Checker interface {
	Check(news scraper.News) bool
	Mark(news scraper.News) bool
}

type InMemoryChecker struct {
	register []scraper.News
}

func New() Checker {
	return InMemoryChecker{
		register: make([]scraper.News, 0),
	}
}

func (checker InMemoryChecker) Check(news scraper.News) bool {
	for _, element := range checker.register {
		if reflect.DeepEqual(element, news) {
			return false
		}
	}
	return true
}

func (checker InMemoryChecker) Mark(news scraper.News) bool {
	checker.register = append(checker.register, news)
	return true
}
