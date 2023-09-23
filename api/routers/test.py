import boto3
from fastapi import FastAPI, UploadFile, File
import os
import uuid
import shutil

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select

from api.services import s3_bucket
from api.services.ipfs import LightHouse



router = APIRouter(
    prefix="/test",
    tags=["test"],
)

@router.post("/upload")
def upload_file(*, file: UploadFile = File(...), tag: str ):
    '''
    TODO: In case of images, check the image and resize it so it does not use uneccessary space

    '''
    # generate unique file name
    name, ext = os.path.splitext(file.filename)
    file.filename = str(uuid.uuid4()) + ext
    path = os.path.join(os.getcwd(), file.filename)

    # save file locally to be able to use the LightHouse Python SDK
    with open(path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    # save in LightHouse
    lh = LightHouse().send_data_lh(path=path, tag=tag)

    # Delete file from local environment
    os.remove(path)
    
    # volver al inicio del archivo
    file.file.seek(0)
    
    # upload to S3
    file.filename = lh['data']['Hash'] + ext
    result = s3_bucket.upload_file(file=file, file_path=file.filename)
    
    return {"web3-LightHouse": lh, 'web2-S3': result}

