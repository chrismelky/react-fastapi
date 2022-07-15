from typing import Any, List
from core.exception import CustomBadRequestException

from schemas import custom_response
from schemas.custom_response import CustomResponse
from schemas.user_schema import User, UserCreate
from fastapi import APIRouter, Depends, Request,HTTPException
from sqlalchemy.orm import Session
from api import deps
from crud.user_crud import userCrud

router = APIRouter()

@router.get('/')
def index(req: Request, db: Session = Depends(deps.get_db)):
    
    query_params = dict(req.query_params)
    page = query_params.pop('page', None)
    size = query_params.pop('size', None)
    columns = query_params.pop('columns', None)

    if page:
        total, result = userCrud.paginate(db,columns=columns, page=page, size=size, search=query_params)
        return CustomResponse(data = result, total= total)
    else:
        result = userCrud.get_all(db,columns=columns,search=query_params)
        return CustomResponse(data = result)

@router.post('/')
def create(in_user: UserCreate, db: Session = Depends(deps.get_db)):
    user = userCrud.find_by_email(db, in_user.email)

    if user: 
        raise CustomBadRequestException(
            message = "Email already taken"
        )
    try:
        result = userCrud.create(db, in_user)
        return CustomResponse(data=result, message='User created successfully')

    except:
        raise HTTPException(
            status_code = 400,
            detail = "Error"
        )

