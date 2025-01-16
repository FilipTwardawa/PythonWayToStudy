import pika
import time


def process_work(ch, method, body):
    print(f"Work processing: {body.decode()}")
    time.sleep(30)
    print(f"Work performed: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_work():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='work_queue')
    channel.basic_consume(queue='work_queue', on_message_callback=process_work)
    print('Awaiting work...')
    channel.start_consuming()


if __name__ == "__main__":
    consume_work()
