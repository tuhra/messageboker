#!/usr/bin/env python
import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()

channel = connection.channel()

channel.queue_declare(queue='hello')

message =  '{ "name":"John", "age":30, "city":"New York"}'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent 'Hello World!'")
connection.close()