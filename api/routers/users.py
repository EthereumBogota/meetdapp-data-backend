'''
Include all the routes starting at /user/
'''
from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.database import get_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users(*, db: Session = Depends(get_session)):
    '''
    TODO
    '''
    return [{"wallet": "Rick"}, {"wallet": "Morty"}]

@router.get("/me")
async def read_user_me(*, db: Session = Depends(get_session)):
    '''
    TODO
    '''
    return {"wallet": "fakecurrentuser"}

@router.get("/{wallet}")
async def read_user(*, db: Session = Depends(get_session), wallet: str):
    '''
    TODO
    '''
    return {"wallet": wallet}


