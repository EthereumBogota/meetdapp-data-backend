'''
Include all the routes starting at /event/
'''
from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.database import get_session

router = APIRouter(
    prefix="/events",
    tags=["events"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_events(*, db: Session = Depends(get_session)):
    return [{"event": "Rick"}, {"event": "Morty"}]

@router.post("/")
async def create_event(*, db: Session = Depends(get_session)):
    return {"created": "ok"}

@router.post("/{event_contract}/assist")
async def create_new_assistant(*, db: Session = Depends(get_session), even_contract: str):
    '''
    TODO: Check if the user wallet can be injected via a dependency (SECURITY)
    '''
    
    return {"registered": "ok"}


@router.get("/{event_contract}")
async def read_event(*, db: Session = Depends(get_session), event_contract: str ):
    return {"event": "this is the event"}



