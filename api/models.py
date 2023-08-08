from sqlmodel import Field, Session, SQLModel, Relationship

from typing import List, Optional
from datetime import datetime



# 'User' Classes -----------------------------
class User(SQLModel, table=True):
    wallet: str = Field(primary_key=True, max_length=50)
    nickname: str = Field(max_length=20)
    cid_img: str = Field(max_length=50)

# 'Group' Classes -----------------------------
class Group(SQLModel, table=True):
    id :  Optional[int] = Field( default=None, primary_key=True)
    name: str = Field(max_length=20)
    events: "Event" = Relationship(back_populates="group")

# 'Event' Classes -----------------------------
class EventBase(SQLModel):
    location: str = Field(index=True)
    y_cord: float
    y_cord: float
    name: str
    event_contract: Optional[int] = Field(default=None, primary_key=True)
    cid_img: str = Field(max_length=50)
    start_date: datetime = Field(index = True)
    end_date: datetime 
    description: str  = Field(max_length=300)
    url: str  = Field(max_length=300)
    key_words: List[str] 

    group_id: int = Field(foreign_key="group.id")
    group: Group = Relationship(back_populates="events")


class Event(EventBase, table=True):
    pass

# class EventCreate(EventBase):
#     pass

# class EventRead(EventBase):
#     pass

# class EventUpdate(SQLModel):
#     pass


# 'EventRegistry' Classes -----------------------------
