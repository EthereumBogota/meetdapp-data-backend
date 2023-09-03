import uvicorn
import api.save_ipfs as sif
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os

from fastapi import FastAPI

# User modules
from api.database import create_db_and_tables, create_users, sqlite_file_name
from api.routers import users, events
import api.save_ipfs as sdata

# ADD dummy data in sqlite database (Only Dev Mode)----
try:
    os.remove(sqlite_file_name)  # START FROM SCRATCH
    print("DB was removed")
except:
    pass
create_db_and_tables()
print("Tables were created")
create_users()
print("Dummy Data was added")
# -------------------------------------

app = FastAPI()


@app.get("/")
def hello_world():
    return {"MeeDapp Api": {"Version": "0.0.1", "Interactive Docs": "/docs", "Docs": "/redoc"}}


@app.get("/save_data_ipfs/")
async def save_data_ipfs(path: str):
    obj_ipfs = sif.lightHouse()
    file_2_ipfs = obj_ipfs.send_data_lh(path=path)

    return file_2_ipfs


@app.get("/download_data/")
async def download_data(cid: str):
    obj_ipfs = sif.lightHouse()
    ipfs_2_file = obj_ipfs.download_data_lh(cid=cid)

    return ipfs_2_file


app.include_router(users.router)
app.include_router(events.router)
