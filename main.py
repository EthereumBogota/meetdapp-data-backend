import uvicorn
import save_ipfs as sdata
from fastapi import FastAPI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()


@app.get("/save_data_ipfs/")
async def save_data_ipfs(path: str):

    print(f"Save data: {path}")

    return path

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8088)
