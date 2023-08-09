import uvicorn
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
    os.remove(sqlite_file_name) # START FROM SCRATCH
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
    print(f"Save data: {path}")
    return path

app.include_router(users.router)
app.include_router(events.router)

