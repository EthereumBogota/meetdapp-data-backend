import boto3
from fastapi import FastAPI, UploadFile, File
import os


AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = os.environ["AWS_SECRET_KEY"]
AWS_REGION = os.environ["AWS_REGION"]
AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]
AWS_BUCKET_URL = os.environ["AWS_BUCKET_URL"]


s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file(*,file: UploadFile = File(...), file_path: str):
    '''
    Upload file to S3

    Params: ---------
    file: file to upload
    path: path to upload file (this should include the file name)

    '''
    s3.upload_fileobj(file.file, AWS_BUCKET_NAME, file_path)
    return {"file": AWS_BUCKET_URL+file_path}
