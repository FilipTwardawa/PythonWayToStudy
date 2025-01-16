import pika

def add_work_to_queue(work):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='work_queue')
    channel.basic_publish(exchange='', routing_key='work_queue', body=work)
    print("Work added to queue")
    connection.close()

if __name__ == "__main__":
    while True:
        new_work = input("Specify the work to be done: ")
        add_work_to_queue(new_work)
