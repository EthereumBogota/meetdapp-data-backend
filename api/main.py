from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


import os



from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# User modules 
from api.services.database import sqlite_file_name, create_db_and_tables
from api.services.dummy_data import create_dummy_data
from api.routers import users, events, ipfs


if os.environ["ENVIRONMENT"] == "PROD":
    pass
else:
    # --------------------------------------
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

description = """
    This api is created to serve the neccesities 
    of the Meet Dapp as IPFS, Users and Events.
"""

app = FastAPI(
    title="Meet Dapp API",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "url": "http://your-website-url.com",  # Replace with your actual website URL
        "email": "your@email.com",  # Replace with your actual email
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

@app.get("/", summary="Root Redirect", description="Redirect to ReDoc Documentation")
async def root_redirect(): return RedirectResponse("/docs")

# ROUTERS
app.include_router(ipfs.router)
app.include_router(users.router)
app.include_router(events.router)
