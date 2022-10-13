#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, 'sync_giep_to_oltms', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='amq.fanout', exchange_type='fanout', durable=True)

message = '{"type": "ONU","info": {"hostname": "MPTX04ZDOY-A02-CA2P16-LCC123455", "gpon_name": "CA1-1111187ZIN-A", "status": "1", signal: "-20.988"}}';
# channel.basic_publish(exchange='amq.fanout', routing_key='', body=message)
channel.basic_publish(
    exchange='amq.fanout',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        correlation_id='12345',
        content_type='application/json',
        delivery_mode=2,  # make message persistent
    )
)

print(" [x] Sent %r" % message)
connection.close()