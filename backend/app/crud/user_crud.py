from crud.base_crud import BaseCrud
from models.user_model import User

class UserCrud(BaseCrud[User]):
    pass

userRepo = UserCrud(User)

