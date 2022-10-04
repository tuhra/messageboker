#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message =  '{ "name":"John", "age":30, "city":"New York"}'

message = ' '.join(sys.argv[1:]) or message
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()