import os
import logging
from logging.handlers import RotatingFileHandler
from sqlalchemy import create_engine
from fastapi import FastAPI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure logging to write to a file
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database")
handler = RotatingFileHandler("app.log", maxBytes=1000000, backupCount=5)  # Rotate log files when they reach 1MB
logger.addHandler(handler)

# Create a database connection URL using environment variables
db_connection_url = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?sslmode={os.getenv('DB_SSL')}"

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        # Attempt to create a database engine and connect to the database
        engine = create_engine(db_connection_url)
        with engine.connect():
            logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")

@app.on_event("shutdown")
async def shutdown_event():
    # Perform any cleanup or shutdown tasks here
    pass

@app.get('/check_db_connection', tags=["database"])
async def check_db_connection():
    # You can add a separate endpoint to check the database connection if needed
    try:
        engine = create_engine(db_connection_url)
        with engine.connect():
            return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": "Database connection failed", "error": str(e)}
