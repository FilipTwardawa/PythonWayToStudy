import json
from uuid import uuid4
import pika
from fastapi import FastAPI, Query
from pydantic import BaseModel
from contextlib import contextmanager

app = FastAPI()

# RabbitMQ connection parameters
RABBITMQ_HOST = 'rabbitmq'
QUEUE_NAME = 'image_tasks'


@contextmanager
def rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    try:
        yield channel
    finally:
        connection.close()


class ImageTask(BaseModel):
    url: str


@app.get("/detect_online_images")
async def detect_online_images(
        urls: str = Query(..., description="Separate multiple URLs with new lines")
):
    url_list = urls.splitlines()
    task_ids = []

    with rabbitmq_connection() as channel:
        for url in url_list:
            task_id = str(uuid4())
            message = {'id': task_id, 'url': url}
            channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message))
            task_ids.append(task_id)

    return {"task_ids": task_ids, "status": "Tasks added to the queue"}
