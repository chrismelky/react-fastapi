from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(passoword: str)->str:
    return pwd_context.hash(passoword)
