from fastapi import APIRouter, Depends, Request, HTTPException, status, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from ..database import get_db
from .. import models, schemas, crud, utils
from typing import List


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/users/")
async def get_users(request: Request, db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    print(all_users)
    context = {"request": request, "users": all_users}
    return templates.TemplateResponse("users.html", context)


@router.get("/users/{username}")
async def get_user(request: Request, username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    user_tags = crud.get_user_tags(db, username)
    context = {"request": request, "user": user, "user_tags": user_tags}
    return templates.TemplateResponse("user_profile.html", context)


@router.post("/register")
async def create_user(request: Request,
                      username: str = Form(...),
                      email: str = Form(...),
                      password: str = Form(...),
                      confirm_password: str = Form(...),
                      tags: List[str] = Form([]),
                      db: Session = Depends(get_db)):

    print(tags)

    errors = {}

    # Username validation
    if crud.get_user_by_username(db, username=username):
        errors["username"] = "Username already in use"

    # Email validation
    if crud.get_user_by_email(db, email=email):
        errors["email"] = "Email already registered"

    # Password confirmation validation
    if password != confirm_password:
        errors["confirm_password"] = "Passwords do not match"

    # Password complexity validation
    if not utils.is_password_valid(password):
        errors[
            "password"] = "Password must be at least 8 characters and include a mix of upper and lower case letters and numbers"

    if len(tags) < 3:
        errors["tags"] = "Select at least three tags"

    # If there are errors, return to the registration page with errors
    if errors:
        return templates.TemplateResponse("register.html", {"request": request,
                                                            "errors": errors,
                                                            "form_data": {"username": username,
                                                                          "email": email}})

    # hash the user's password and create a new user record
    hashed_password = utils.hash_password(password)
    new_user = models.User(username=username, email=email, hashed_password=hashed_password)
    db.add(new_user)

    # add interest tags to the user
    for tag_id in tags:
        tag = db.query(models.Tag).get(int(tag_id))
        if tag:
            new_user.tags.append(tag)

    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    all_tags = db.query(models.Tag).all()
    context = {"request": request, "errors": {}, "form_data": {}, "tags": all_tags}
    return templates.TemplateResponse("register.html", context)


@router.get("/login")
async def login(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("login.html", context)
