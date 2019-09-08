FROM golang:1.13.0-buster
RUN mkdir /opt/app
COPY . /opt/app
WORKDIR /opt/app
ENTRYPOINT ./scripts/run-app.sh