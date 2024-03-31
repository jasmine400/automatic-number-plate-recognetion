from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from Anpr import detection
from Anpr import segmentaion
import cv2
# from cv2  import dnn_superres
import torch
from skimage.io import imread_collection
from ultralytics import YOLO
from cv2 import dnn_superres
import uvicorn
from typing import List
# yolo = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# my_model = YOLO('weights_segment/best.pt')
IMAGEDIR = "images/"
 
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/images", StaticFiles(directory="images"), name="images")
 
@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
 
@app.post("/upload-files")
async def create_upload_files(request: Request, files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        #save the file
        with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
            f.write(contents)
 
    # show = [file.filename for file in files]
    detection()
    resultt  = segmentaion()
    dic={}
    #return {"Result": "OK", "filenames": [file.filename for file in files]}
    return resultt

if __name__ == '__main__':
    uvicorn.run(app, port=8000,host='127.0.0.1')