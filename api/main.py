import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

import api.save_ipfs as sdata
from api.database import create_db_and_tables, engine
from api.models import User, Event


# Load environment variables from .env file
load_dotenv()
app = FastAPI()


@app.get("/save_data_ipfs/")
async def save_data_ipfs(path: str):

    print(f"Save data: {path}")

    return path

if __name__ == '__main__':
    create_db_and_tables()
    print("Tables were created")
    uvicorn.run(app, host='0.0.0.0', port=8088)

