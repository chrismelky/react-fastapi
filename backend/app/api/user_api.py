from typing import Any, List
from schemas import custom_response
from schemas.custom_response import CustomResponse
from schemas.user_schema import User, UserCreate
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from api import deps
from crud.user_crud import userRepo

router = APIRouter()

@router.get('/')
def index(req: Request, db: Session = Depends(deps.get_db)):
    
    query_params = dict(req.query_params)
    page = query_params.pop('page', None)
    size = query_params.pop('size', None)
    columns = query_params.pop('columns', None)

    if page:
        total, result = userRepo.paginate(db,columns=columns, page=page, size=size, search=query_params)
        return CustomResponse(data = result, total= total)
    else:
        result = userRepo.get_all(db,columns=columns,search=query_params)
        return CustomResponse(data = result)

@router.post('/')
def create(user: UserCreate, db: Session = Depends(deps.get_db)):
    pass
