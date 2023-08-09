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

app = FastAPI()

@app.get("/save_data_ipfs/")
async def save_data_ipfs(path: str):
    print(f"Save data: {path}")
    return path

app.include_router(users.router)
app.include_router(events.router)



if __name__ == '__main__':
    os.remove(sqlite_file_name) # START FROM SCRATCH
    create_db_and_tables()
    print("Tables were created")
    create_users()
    print("Users were added")
    uvicorn.run(app, host='0.0.0.0', port=8088)

