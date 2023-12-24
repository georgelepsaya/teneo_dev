from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .api import users
from .auth import router as auth_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(users.router)
app.include_router(auth_router)


@app.get("/")
async def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

