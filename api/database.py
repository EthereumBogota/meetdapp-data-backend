'''
Conection to Database
'''

from sqlmodel import SQLModel, create_engine, Session
from api.models import User, Event, Group



sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_users():
    
    session = Session(engine)

    user_1 = User(wallet="123", nickname="123nick", cid_img="cid123")
    user_2 = User(wallet="567", nickname="567nick", cid_img="cid567")
    user_3 = User(wallet="890", nickname="890nick", cid_img="cid890")

    group_1 = Group(name="Ethereum")
    group_1.users = [user_1, user_2]
    session.add(group_1)
    session.commit()

    event_dict = {
        "location": "string",
        "y_cord": 0,
        "x_cord": 0,
        "name": "string",
        "event_contract": "contract123",
        "cid_img": "string",
        "start_date": "2023-08-08T23:19:02.809Z",
        "end_date": "2023-08-08T23:19:02.809Z",
        "description": "string",
        "url": "string",
        "key_words": "keywords",
        "group_id": group_1.id
    }

    event = Event(**event_dict)

    session.add(group_1)
    session.add(user_3)
    session.add(event)

    session.commit()
    session.close()

    

# Connect to DB Session Dependency
def get_session():
    with Session(engine) as session:
        yield session