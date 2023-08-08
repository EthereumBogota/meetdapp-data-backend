'''
Conection to Database
'''

from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Connect to DB Session Dependency
def get_session():
    with Session(engine) as session:
        yield session