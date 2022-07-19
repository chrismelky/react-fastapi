from typing import Any, Generic, List, Type, TypeVar
from db.base_model import Base
from sqlalchemy.orm import Session, load_only, Query
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


ModelType = TypeVar('ModelType', bound=Base)
CreateModelType = TypeVar('CreateModelType', bound=BaseModel)
UpdateModelType = TypeVar('UpdateModelType', bound=BaseModel)

class BaseCrud(Generic[ModelType,CreateModelType,UpdateModelType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model
    
    def get_all(self, db: Session, columns:str | None = None, search = {})->List[ModelType]:
        query = self.allQuery(db, columns, search)
        return query.all()
    
    def paginate(self , db: Session, page = 0, size = 10, columns:str | None = None, search = {} )-> Any:
        query = self.allQuery(db, columns, search)
        total = query.count()
        result = query.offset(0).limit(size).all()
        return (total, result)
    
    def find_by_id(self, db: Session, id)->ModelType | None:
        return db.query(self.model).filter(ModelType.id == id).first()


    def allQuery(self, db: Session, columns:str | None = None, search = {}) -> Query:
        query = db.query(self.model)
        if columns :
            query = query.options(load_only(*columns.split(',')))
        
        if len(search) > 0:
            for k, v in search.items():
                query = query.filter(getattr(self.model, k).ilike('%{}%'.format(v)))
        return query

    def create(self, db: Session, in_obj: CreateModelType)->ModelType:
        in_obj_data = jsonable_encoder(in_obj)
        db_obj = self.model(**in_obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, db_object, in_object)->ModelType:
        db_obj_data = jsonable_encoder(db_object)

    def remove(self, db:Session, id: int):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()


    