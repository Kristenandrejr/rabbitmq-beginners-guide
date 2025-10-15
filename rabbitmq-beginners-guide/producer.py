# producer.py
# Simple RabbitMQ producer example
# Make sure RabbitMQ is installed and running on your system

import pika

# Connect to RabbitMQ server on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue named 'hello'
channel.queue_declare(queue='hello')

# Send a message
channel.basic_publish(exchange='', routing_key='hello', body='Hello from RabbitMQ!')

print(" [x] Sent 'Hello from RabbitMQ!'")

# Close the connection
connection.close()
