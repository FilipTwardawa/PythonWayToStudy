from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image
import requests
from io import BytesIO

app = FastAPI()
yolo_model = YOLO('yolov9c.pt')


def detect_persons_in_image(image: Image):
    return yolo_model.predict(source=image, classes=[0], conf=0.4)[0] if image else None


def save_image_to_disk(image: Image, path: str):
    image.save(path)


def process_bytes_to_image(data: bytes) -> Image:
    return Image.open(BytesIO(data))


async def detect_persons_in_uploaded_image(image):
    result_image = detect_persons_in_image(image)
    if result_image:
        save_path = "result.jpg"
        save_image_to_disk(result_image, save_path)
        return {"Liczba wykrytych osób na obrazie: ": len(result_image.boxes), "Wynik zapisano w pliku: ": save_path}
    raise HTTPException(status_code=500, detail="Nie wykryto osób na obrazie.")


@app.get("/detect_local_image")
async def detect_persons_in_local_image(file_path: str):
    try:
        return await detect_persons_in_uploaded_image(Image.open(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/detect_online_image")
async def detect_persons_in_online_image(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return await detect_persons_in_uploaded_image(Image.open(BytesIO(response.content)))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/detect_uploaded_image")
async def detect_persons_in_uploaded_image_endpoint(file: UploadFile = File(...)):
    try:
        return await detect_persons_in_uploaded_image(process_bytes_to_image(await file.read()))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
