'''
Include all the routes starting at /user/
'''
from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.services.database import get_session 
from api.models.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users(*, db: Session = Depends(get_session)):
    '''
    TODO: not created yet
    '''
    return [{"wallet": "Rick"}, {"wallet": "Morty"}]

@router.patch("/web3_confirm")
async def web3_confirm(*, wallet: str, db: Session = Depends(get_session)):
    '''
    Confirm the creation of an EVENT from the web3 
    '''
    user = db.exec(select(User).where(User.wallet == wallet)).one()
    if not user:
        return {"confirmed": "failed"} 
    user.web3_confirmed = True
    db.add(user)
    db.commit()
    db.refresh(user)
    db.commit()
    return {"confirmed": "ok"}

@router.get("/me")
async def read_user_me(*, db: Session = Depends(get_session)):
    '''
    TODO: not created yet
    '''
    return {"wallet": "fakecurrentuser"}

@router.post("/{wallet}")
async def read_user(*, db: Session = Depends(get_session), wallet: str):
    '''
    TODO: not created yet
    '''
    return {"wallet": wallet}




@router.get("/{wallet}")
async def read_user(*, db: Session = Depends(get_session), wallet: str):
    '''
    TODO: not created yet
    '''
    return {"wallet": wallet}



