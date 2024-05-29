***
***
# Application : Detecting People in Pictures Using FastAPI, RabbitMQ and YOLO
***
***


## Description of the project

This project enables the detection of people in images available online. It uses the YOLO model for this, which is one of the latest methods for detecting objects in images. The system consists of two main components: a RabbitMQ consumer that retrieves detection tasks from a queue, and a FastAPI application that allows new tasks to be added to the queue.
***

## Architecture

- **RabbitMQ**: Message broker that stores the tasks to be executed.
- **FastAPI**: A web framework for adding tasks to a queue.
- **YOLO**: A model for detecting people in pictures.
- **Docker**: Application containerisation tool.
***
## Project files

- `Consumer.py`: RabbitMQ consumer handler script.
- `Producer.py`: Script serving the FastAPI application.
- `Dockerfile`: Configuration file for Docker, defining the container image.
- `docker-compose.yml`: Configuration file for Docker Compose, enabling the entire application to run.
***
    app/
    ├── Consumer.py # RabbitMQ consumer script
    ├─── Producer.py # FastAPI application script
    ├─── Dockerfile # Docker image definition file
    ├── docker-compose.yml # Configuration file for Docker Compose
    └── results/ # Directory where processed images will be saved
***
## Commissioning instructions

### Requirements

- Docker
- Python 12 or higher version

### Steps

1. **Clone the repository**.

   ```bash
   git clone git@github.com:FilipTwardawa/ZPwJpython_ZD_FT.git
   cd ZPwJpython_ZD_FT

2. **Start the application using Docker Compose**.

   ```bash
   docker-compose up --build
   
3. **Starting the application**.
   * Open a browser and navigate to:
      ```bash
       https://localhost:15672/
   - log in to RabbitMQ (login and password : guest)
   * Open the index.html file


4. **Enjoy the application**.
***