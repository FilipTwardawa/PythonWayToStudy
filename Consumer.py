import json
import pika
import requests
from PIL import Image
from io import BytesIO
from ultralytics import YOLO
import os
import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# YOLO model initialization
yolo_model = YOLO('yolov9c.pt')

# RabbitMQ connection parameters
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'image_tasks'
RESULT_DIR = 'results'

if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)


def detect_persons_in_image(image: Image):
    return yolo_model.predict(source=image, classes=[0], conf=0.4)[0] if image else None


def save_image_to_disk(image: Image, path: str):
    image.save(path)


def process_bytes_to_image(data: bytes) -> Image:
    return Image.open(BytesIO(data))


class RabbitMQConsumer:
    def __init__(self, host, queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_qos(prefetch_count=1)
        self.queue_name = queue_name

    def start_consuming(self, callback):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
        logging.info('Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.stop_consuming()
        self.connection.close()


def process_task(ch, method, properties, body):
    task_id = None
    try:
        task = json.loads(body)
        task_id = task['id']
        url = task['url']

        logging.info(f"Processing task {task_id} with URL: {url}")

        response = requests.get(url)
        response.raise_for_status()
        image = process_bytes_to_image(response.content)

        result_image = detect_persons_in_image(image)
        if result_image:
            person_count = len(result_image.boxes)
            file_extension = url.split('.')[-1]
            save_path = os.path.join(RESULT_DIR, f"{task_id}-{person_count}.{file_extension}")
            save_image_to_disk(result_image, save_path)
            logging.info(f"Task {task_id} completed. Image saved to {save_path}")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON: {e}, body: {body}")
        ch.basic_nack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logging.error(f"Task {task_id if task_id else 'unknown'} failed: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)


def start_consumer():
    consumer = RabbitMQConsumer(RABBITMQ_HOST, QUEUE_NAME)
    try:
        consumer.start_consuming(process_task)
    except KeyboardInterrupt:
        consumer.stop_consuming()


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(start_consumer)
