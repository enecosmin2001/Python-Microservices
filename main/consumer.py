import pika 

params = pika.URLParameters('amqps://btwdpfjz:KY6sejA6-DMijyCDO8I0Hz3kgk4A-wrE@chimpanzee.rmq.cloudamqp.com/btwdpfjz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()