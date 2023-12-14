from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, get_db
from . import models
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .api import users

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(users.router)

@app.get("/")
async def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

