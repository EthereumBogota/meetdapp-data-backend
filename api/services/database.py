'''
Conection to Database
'''

from sqlmodel import SQLModel, create_engine, Session

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




