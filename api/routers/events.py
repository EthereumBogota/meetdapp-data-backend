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
    TODO: Test
    '''
    events = db.exec(select(Event).offset(offset).limit(limit)).all()
    return events

@router.patch("/web3_confirm")
async def web3_confirm(*, contract_id: str, db: Session = Depends(get_session)):
    '''
    Confirm the creation of an EVENT from the web3 
    '''
    event = db.exec(select(Event).where(Event.event_contract == contract_id)).one()
    if not event:
        return {"confirmed": "failed", "message": "Event not found"} 
    event.web3_confirmed = True
    db.add(event)
    db.commit()
    db.refresh(event)
    db.commit()
    return {"confirmed": "ok"}

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
async def read_event(*,  event_id: str, db: Session = Depends(get_session) ):
    '''
    TODO: Test
    '''
    db_event = db.get(Event, event_id)
    if not db_event:
        return {"message": "event not found"}
    return db_event

@router.patch("/{event_contract}")
async def update_event(*, updated_event: Event , event_id: str, db: Session = Depends(get_session) ):
    '''
    Update event by event_id
    TODO: Make model of update_event parameter, to make only the editable values are changed
    '''
    existing_event = db.get(Event, event_id)
    if not existing_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    for key, value in updated_event.dict().items():
        setattr(existing_event, key, value)


    db.commit()
    db.refresh(existing_event)
    return existing_event

@router.delete("/{event_contract}")
async def delete_event(*,  event_id: str, db: Session = Depends(get_session) ):
    '''
    TODO: Delete event
    '''
    db_event = db.get(Event, event_id)
    if not db_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    db.delete(db_event)
    db.commit()
    return {"status": "deleted"}

@router.post("/{event_contract}/assist")
async def create_new_assistant(*, event_id: str, wallet: str, db: Session = Depends(get_session)):
    '''
    TODO: Check if the user_wallet can be injected via a dependency (SECURITY)
    '''
    db_user = db.get(User, wallet)
    db_event = db.get(Event, event_id)
    if not db_user:
        return {"registered": "failed", "info": "User not found"}
    # if not db_event:
    #     return {"registered": "failed", "info": "Event not found"}
    
    registration = EventRegistry(event_id=db_event.event_contract, 
                                 user_wallet=db_user.wallet,
                                 status=EventRegistryStatusEnum.REGISTERED)
    
    db.add(registration)
    db.commit()

    return {"registered": "ok"}


