'''
Conection to Database
'''

from sqlmodel import SQLModel, create_engine, Session

import os 


sqlite_file_name = ""

if os.environ["ENVIRONMENT"] == "PROD":
    print("CONNECTING TO PRODUCTION DATABASE")
    DB_USERNAME = os.environ["DB_USERNAME"]
    DB_PASSWORD = os.environ["DB_PASSWORD"] 
    DB_PORT = os.environ["DB_PORT"]
    DB_URL = os.environ["DB_URL"]
 
    DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}:{DB_PORT}/meedapp_db"
    engine = create_engine(DATABASE_URL, 
                         #echo=True,  # UNCOMMENT THIS LINE IF YOU WHANT TO SEE ALL THE DATABASE LOGS
                        )
    

else:
    print("CONNECTING TO DEVELOP DATABASE")

    sqlite_file_name = "api/database.sqlite"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, 
                        #    echo=True,  # UNCOMMENT THIS LINE IF YOU WHANT TO SEE ALL THE DATABASE LOGS
                        connect_args=connect_args
                        )

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Connect to DB Session Dependency
def get_session():
    with Session(engine) as session:
        yield session




