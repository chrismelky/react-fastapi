from core.security import get_password_hash
from schemas.user_schema import UserCreate, UserUpdate
from crud.base_crud import BaseCrud
from models.user_model import User
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

class UserCrud(BaseCrud[User, UserCreate, UserUpdate]):

    def create(self, db: Session, in_obj: UserCreate) -> User:
        db_object = User(
            **jsonable_encoder(in_obj),
            password_hash = get_password_hash("Secret1234")
        )
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    def find_by_email(self, db, email: str)->User | None:
        return db.query(User).filter(User.email == email).first()

userCrud = UserCrud(User)

