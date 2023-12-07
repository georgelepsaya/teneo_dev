from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, get_db
from . import models
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root(request: Request):
    context = {"request": request, "message": "Hello, World!"}
    return templates.TemplateResponse("index.html", context)


@app.get("/users")
async def users(request: Request, db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    context = {"request": request, "users": users}
    return templates.TemplateResponse("users.html", context)
