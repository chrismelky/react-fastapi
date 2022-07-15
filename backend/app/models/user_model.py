from db.base_model import Base
from sqlalchemy import Column, String, Integer, Boolean

class User(Base):

    __tablename__= "users"

    id = Column(Integer, primary_key= True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    email = Column(String, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
