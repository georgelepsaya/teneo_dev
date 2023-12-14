from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from ..database import get_db
from .. import models, schemas, crud, utils


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/users/")
async def get_users(request: Request, db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    print(all_users)
    context = {"request": request, "users": all_users}
    return templates.TemplateResponse("users.html", context)


@router.post("/register")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if the user already exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")

    # hash the user's password and create a new user record
    hashed_password = utils.hash_password(user.password)
    user_dict = user.model_dump()
    print(user_dict)
    user_dict['hashed_password'] = hashed_password
    del user_dict['password']
    new_user = models.User(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    return templates.TemplateResponse("register.html", context)
