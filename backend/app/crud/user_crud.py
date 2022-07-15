from core.security import get_password_hash
from schemas.user_schema import UserCreate, UserUpdate
from crud.base_crud import BaseCrud
from models.user_model import User
from sqlalchemy.orm import Session

class UserCrud(BaseCrud[User, UserCreate, UserUpdate]):

    def create(self, db: Session, in_obj: UserCreate) -> User:
        db_object = User(
            first_name= in_obj.first_name,
            last_name = in_obj.last_name,
            email = in_obj.email,
            is_active = in_obj.is_active,
            password_hash = get_password_hash("Secret1234")
        )
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    def find_by_email(self, db, email: str)->User | None:
        return db.query(User).filter(User.email == email).first()

userCrud = UserCrud(User)

