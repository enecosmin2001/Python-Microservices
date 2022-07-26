import pika, json

params = pika.URLParameters('amqps://zjdpztgf:YqG4aibENmEjIP53I_egIJuXbNWTD3Ba@moose.rmq.cloudamqp.com/zjdpztgf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    print(f"Sending producer body: {json.dumps(body)}")
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

