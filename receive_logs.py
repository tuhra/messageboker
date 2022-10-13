#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, 'sync_giep_to_oltms', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# result = channel.queue_declare(queue='giep_to_oltms_queue', durable=True, arguments={'x-message-ttl' : 60000})
# queue_name = result.method.queue
# channel.queue_bind(exchange='amq.fanout', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='giep_to_oltms_queue', on_message_callback=callback)
channel.start_consuming()