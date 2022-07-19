from sys import prefix
from turtle import title
from core.exception import CustomBadRequestException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.routes import api_router

app = FastAPI(
    title= 'Starter'
)



@app.exception_handler(CustomBadRequestException)
async def bad_request_exception_handle(request: Request,exc: CustomBadRequestException):
    return JSONResponse(
        status_code = 400,
        content = {
            "message": exc.message,
            "errors": exc.errors,
            "status_code": 400
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = map(lambda d: f"{d.get('loc')[1]} {d.get('msg')}", exc.errors())
    errors = list(errors)
    return JSONResponse(
        status_code = 400,
        content = {
            "message": "Validation Error",
            "errors": errors,
            "status_code": 400
        }
    )

app.include_router(api_router, prefix="/api")

