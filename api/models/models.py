'''
Classes containing the shape of the data f
'''

from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime
from enum import Enum

# 'User' Classes -----------------------------
class User(SQLModel, table=True):
    wallet: str = Field(primary_key=True, max_length=50)
    nickname: str = Field(max_length=20)
    cid_img: Optional[str] = Field(default=None, max_length=50)
    web3_confirmed: Optional[bool] = Field(default=False)

    user_registry_links: List["EventRegistry"] = Relationship(back_populates="users")


# 'Event' Classes -----------------------------
class Event(SQLModel, table=True):
    # Data saved in Blockchain
    event_id: str = Field(default=None, primary_key=True, max_length=50) ## an special nano_id that is also the id on the Blockchain
    name: str
    description: str  
    location: str = Field(index=True)
    nft_name : str = Field(max_length=30)
    nft_symbol : str = Field(max_length=30)
    nft_uri : str = Field(max_length=50)
    start_date: datetime = Field(index = True)
    end_date: datetime 
    capacity: int

    # aditional data not saved in blockchain
    y_cord:Optional[float]
    x_cord: Optional[float]
    # ipfs
    cid_img: str = Field(max_length=50)
    key_words: Optional[str]
    web3_confirmed: Optional[bool] = Field(default=False)


    event_registry_links: List["EventRegistry"] = Relationship(back_populates="events")

# 'EventRegistry' Classes -----------------------------
class EventRegistryStatusEnum(str, Enum):
    '''
    Possible event status for the EventRegistry status field.
    '''
    REGISTERED = 'registered'
    CANCELLED = 'cancelled'
    ASISTED = 'asisted'
    
class EventRegistry(SQLModel, table=True):
    '''
    Link between Events and Users
    '''
    event_id: str = Field(foreign_key="event.event_id", primary_key=True)
    user_wallet: str = Field(foreign_key="user.wallet", primary_key=True)

    status: EventRegistryStatusEnum
    log_date: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False, index=True)
    web3_confirmed: Optional[bool] = Field(default=False)


    users: List[User] = Relationship(back_populates="user_registry_links")
    events: List[Event] = Relationship(back_populates="event_registry_links")
