# PythonWayToStudy

---

# Person Detection API using YOLOv9

**This FastAPI-based project utilizes a YOLOv9 model to detect persons in images. It provides endpoints to analyze images from local files, online URLs, or directly uploaded files.**

## Features

- Detect persons in images with a confidence threshold of 40%.
- Accepts images as:
  - File uploads via POST requests.
  - URLs pointing to online images.
  - Local file paths.
- Saves processed images with detection results locally.

---

## Installation

### Prerequisites
- Python 3.8+
- Install the required Python packages:

```bash
  pip install fastapi uvicorn ultralytics pillow requests
```
## Clone the Repository

````bash
  git clone <git@github.com:FilipTwardawa/PythonWayToStudy.git>
  cd <repository_directory>
  git checkout person_detection
````

---

## Usage

Start the Server
Run the API server locally:

```bash
  uvicorn main:app --reload
```

---

## API Endpoints

1. Detect Persons in Local Image

    GET /detect_local_image

- Parameters:
  - file_path (str): Path to the local image file.
  
- Response:
  - Liczba wykrytych osób na obrazie (number of persons detected).
  - Wynik zapisano w pliku (path to the result image).


2. Detect Persons in Online Image

    GET /detect_online_image

- Parameters:
  - url (str): URL to the image.
  
- Response:
  - Liczba wykrytych osób na obrazie (number of persons detected).
  - Wynik zapisano w pliku (path to the result image).


3. Detect Persons in Uploaded Image

    POST /detect_uploaded_image

- Parameters:
  - Upload an image file using multipart/form-data.
  
- Response:
  - Liczba wykrytych osób na obrazie (number of persons detected).
  - Wynik zapisano w pliku (path to the result image).

---