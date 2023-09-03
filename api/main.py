from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

import os

from fastapi import FastAPI

# User modules 
from api.services.database import   sqlite_file_name, create_db_and_tables
from api.services.dummy_data import create_dummy_data
from api.routers import users, events, ipfs



#--------------------------------------
# CREATING DUMMY DATABASE AND DATA
# ADD dummy data in sqlite database (Only Dev Mode)----
try:
    os.remove(sqlite_file_name)  # START FROM SCRATCH
    print("DB was removed")
except:
    pass
create_db_and_tables()
print("Tables were created")
create_dummy_data()
# -------------------------------------

app = FastAPI()


@app.get("/")
def hello_world():
    return {"MeeDapp Api": {"Version": "0.0.1", "Interactive Docs": "/docs", "Docs": "/redoc"}}


app.include_router(ipfs.router)
app.include_router(users.router)
app.include_router(events.router)
