FROM rabbitmq:management-alpine

COPY ./rabbitmq.config /etc/rabbitmq/
COPY ./definitions.json /etc/rabbitmq/

RUN chmod 777 /etc/rabbitmq/rabbitmq.config