import pika 

params = pika.URLParameters('amqps://btwdpfjz:KY6sejA6-DMijyCDO8I0Hz3kgk4A-wrE@chimpanzee.rmq.cloudamqp.com/btwdpfjz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')

