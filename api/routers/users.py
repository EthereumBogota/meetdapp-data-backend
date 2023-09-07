from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select

from api.services.database import get_session 
from api.models.models import User


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=list[User])
async def read_users(db: Session = Depends(get_session),
                    offset: int = 0,
                    limit: int = Query(default=100, lte=100),
                    ):
    """
    Get a list of all users.
    """
    users = db.query(User).offset(offset).limit(limit).all()
    return users

@router.post("/", response_model=User)
async def create_user(user: User, db: Session = Depends(get_session)):
    """
    Create a new user.
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

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

@router.get("/{wallet}")
async def read_user(*, wallet: str,db: Session = Depends(get_session)):
    '''
    TODO: Create a return model to not disclose extra information
    Returns the information about a user
    '''
    user = db.get(User, wallet)
    return user




@router.put("/{wallet}", response_model=User)
async def update_user(wallet: str, updated_user: User, db: Session = Depends(get_session)):
    """
    Update user details by wallet address.
    """
    existing_user = db.query(User).filter(User.wallet == wallet).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    for key, value in updated_user.dict().items():
        setattr(existing_user, key, value)


    db.commit()
    db.refresh(existing_user)
    return existing_user

@router.delete("/{wallet}", response_model=User)
async def delete_user(wallet: str, db: Session = Depends(get_session)):
    """
    TODO: check if user should be returned or it should be better if return a message of "deleted"
    Delete user by wallet address.
    """
    user = db.query(User).filter(User.wallet == wallet).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    db.delete(user)
    db.commit()
    return user
