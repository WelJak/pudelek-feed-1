package configloader

import (
	"errors"
	"github.com/joho/godotenv"
	"os"
	"strconv"
	"strings"
)

const WebsiteUrl = "https://se.pl"
const envConfigPath = "configs/"

const rabbitHost = "RABBIT_HOST"
const rabbitLogin = "RABBIT_LOGIN"
const rabbitPassword = "RABBIT_PASSWORD"
const rabbitExchange = "RABBIT_EXCHANGE"
const rabbitVhost = "RABBIT_VHOST"
const rabbitRoutingKey = "RABBIT_ROUTING_KEY"
const sleepTimeInSeconds = "SLEEP_TIME_IN_SECONDS"

type Config struct {
	RabbitHost         string
	RabbitLogin        string
	RabbitPassword     string
	RabbitExchange     string
	RabbitVhost        string
	RabbitRoutingKey   string
	SleepTimeInSeconds int64
}

func Getenv(key, fallback string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		return fallback
	}
	return value
}

func getenvOrPanic(key string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		panic(errors.New("Environment variable with key: " + key + " doesn't exist"))
	}
	return value
}

func loadEnvConf(env string) {
	lowerCaseEnv := strings.ToLower(env)
	_ = godotenv.Load(envConfigPath + ".env." + lowerCaseEnv + ".local")
	if "test" != lowerCaseEnv {
		_ = godotenv.Load(envConfigPath + ".env.local")
	}
	_ = godotenv.Load(envConfigPath + ".env." + lowerCaseEnv)
	_ = godotenv.Load(envConfigPath + ".env")
}

func Load(env string) *Config {
	loadEnvConf(env)
	host := getenvOrPanic(rabbitHost)
	login := getenvOrPanic(rabbitLogin)
	password := getenvOrPanic(rabbitPassword)
	exchange := getenvOrPanic(rabbitExchange)
	vhost := getenvOrPanic(rabbitVhost)
	routingKey := getenvOrPanic(rabbitRoutingKey)
	sleepTime, _ := strconv.ParseInt(getenvOrPanic(sleepTimeInSeconds), 10, 64)
	return &Config{
		RabbitHost:         host,
		RabbitLogin:        login,
		RabbitPassword:     password,
		RabbitExchange:     exchange,
		RabbitVhost:        vhost,
		RabbitRoutingKey:   routingKey,
		SleepTimeInSeconds: sleepTime,
	}
}
