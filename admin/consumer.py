import pika
import json

import django
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://zjdpztgf:YqG4aibENmEjIP53I_egIJuXbNWTD3Ba@moose.rmq.cloudamqp.com/zjdpztgf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print(f"Recived {body}")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_liked':
        product = Product.objects.get(id=data['id'])
        product.likes = product.likes + 1
        product.save()
        print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()