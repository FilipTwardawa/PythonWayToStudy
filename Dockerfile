# Set the base Python image
FROM python:3.12-slim

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install required packages
RUN pip install --no-cache-dir fastapi uvicorn pika pydantic requests pillow ultralytics

# Expose the port to the outside
EXPOSE 8000

# Command to run the FastAPI application and RabbitMQ consumer
CMD ["sh", "-c", "python Consumer.py & uvicorn Producer:app --reload --host=0.0.0.0 --port=8000"]
