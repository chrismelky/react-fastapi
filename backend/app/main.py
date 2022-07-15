from sys import prefix
from turtle import title
from fastapi import FastAPI
from api.routes import api_router

app = FastAPI(
    title= 'Starter'
)

app.include_router(api_router, prefix="/api")

