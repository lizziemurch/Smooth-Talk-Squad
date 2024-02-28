import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sts_backend.audio.splitter import splitter
import os
import numpy as np

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

UPLOAD_DIRECTORY = os.path.join("sts_backend","audio","uploads")

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# http://127.0.0.1:8000/predict
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):

    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    print(file_location)
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    splitter(file.filename, file_location)

    #### FOR LOOP splits folder and RUN THE MODEL HERE ####

    # The audio clips are in splits folder
    return {"filename": file.filename, "file_location": file_location}



@app.get("/")
def root():
    params = {'greeting': 'Hello'}
    return params
