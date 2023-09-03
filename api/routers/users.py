from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from api.services.database import get_session
from api.models.models import User


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=list[User])
async def read_users(db: Session = Depends(get_session)):
    """
    Get a list of all users.
    """
    users = db.query(User).all()
    return users

@router.get("/{wallet}", response_model=User)
async def read_user(wallet: str, db: Session = Depends(get_session)):
    """
    Get user details by wallet address.
    """
    user = db.query(User).filter(User.wallet == wallet).first()
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )

@router.post("/", response_model=User)
async def create_user(user: User, db: Session = Depends(get_session)):
    """
    Create a new user.
    """
    db.add(user)
    db.commit()
    db.refresh(user)
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
