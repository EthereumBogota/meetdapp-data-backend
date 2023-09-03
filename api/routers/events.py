'''
Include all the routes starting at /event/
'''
from fastapi import APIRouter, Depends, Query

from sqlmodel import Session, select
from typing import List
from api.services.database import get_session
from api.models.models import User, Event, EventRegistry, EventRegistryStatusEnum

router = APIRouter(
    prefix="/events",
    tags=["events"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Event])
async def read_events(*, 
                      offset: int = 0,
                      limit: int = Query(default=100, lte=100),
                      db: Session = Depends(get_session)
                      ):
    '''
    TODO: not created yet
    '''
    events = db.exec(select(Event).offset(offset).limit(limit)).all()
    return events

@router.post("/new_event", response_model=Event)
async def create_event(*, event: Event, db: Session = Depends(get_session)):
    '''
    Create a new event 
    TODO: 
        - verify user permissions to create event
        - Give useful info when failed 
    '''
    db.add(event)
    db.commit()
    return {"created": "ok"}


@router.get("/{event_contract}")
async def read_event(*,  event_contract: str, db: Session = Depends(get_session) ):
    '''
    TODO: not created yet
    '''
    return {"event": "this is the event"}

@router.post("/{event_contract}/assist")
async def create_new_assistant(*, event_contract: str, wallet: str, db: Session = Depends(get_session)):
    '''
    TODO: Check if the user_wallet can be injected via a dependency (SECURITY)
    '''
    db_user = db.get(User, wallet)
    db_event = db.get(Event, event_contract)
    if not db_user:
        return {"registered": "failed", "info": "User not found"}
    # if not db_event:
    #     return {"registered": "failed", "info": "Event not found"}
    
    registration = EventRegistry(event_contract=db_event.event_contract, 
                                 user_wallet=db_user.wallet,
                                 status=EventRegistryStatusEnum.REGISTERED)
    
    db.add(registration)
    db.commit()

    return {"registered": "ok"}


