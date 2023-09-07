from sqlmodel import Session
from api.services.database import engine
from api.models.models import User, Event #, Group


def create_dummy_data():
    
    session = Session(engine)

    user_1 = User(wallet="0x4aDc123", nickname="Alice", cid_img="QmXyz123")
    user_2 = User(wallet="0x8BbE567", nickname="Bob", cid_img="QmAbc456")
    user_3 = User(wallet="0xCcEf890", nickname="Charlie", cid_img="QmDef789")



    session.add(user_1)
    session.add(user_2)
    session.add(user_3)

    session.commit()


    event_dict = {
    "event_id": "12345",
    "name": "Sample Event",
    "description": "This is a sample event description.",
    "location": "Sample Location",
    "nft_name": "Sample NFT",
    "nft_symbol": "SNFT",
    "nft_uri": "https://example.com/sample-nft",
    "start_date": "2023-09-06T10:00:00Z",
    "end_date": "2023-09-06T18:00:00Z",
    "capacity": 100,
    "y_cord": 123.456,
    "x_cord": 789.012,
    "cid_img": "QmXyz123",
    "key_words": "sample, event, keywords",
    "web3_confirmed": True
    }


    event = Event(**event_dict)

    # session.add(group_1)
    session.add(user_3)
    session.add(event)

    session.commit()
    
    print("Dummy Data was added")
    