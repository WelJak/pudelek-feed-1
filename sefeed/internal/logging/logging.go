package logging

import (
	"github.com/sirupsen/logrus"
	"os"
)

type LoggerFactory struct {
	level logrus.Level
}

var logLevelMap = map[string]logrus.Level{
	"LOCAL": logrus.DebugLevel,
	"DEV":   logrus.DebugLevel,
	"LIFE":  logrus.InfoLevel,
}

var loggerFactory *LoggerFactory

func InitLoggerFactory(env string) *LoggerFactory {
	if loggerFactory == nil {
		logLevel := logLevelMap[env]
		loggerFactory = &LoggerFactory{level: logLevel}
	}
	return loggerFactory
}

func CreateLogger() *logrus.Logger {
	if loggerFactory == nil {
		panic("LoggerFactory not initialized")
	}
	return loggerFactory.CreateLogger()
}

func (l LoggerFactory) CreateLogger() *logrus.Logger {
	log := logrus.New()
	log.SetFormatter(&logrus.TextFormatter{
		FullTimestamp: true,
	})
	log.SetLevel(l.level)
	log.SetReportCaller(true)
	log.SetOutput(os.Stdout)
	return log
}
