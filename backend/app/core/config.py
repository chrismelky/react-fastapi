from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn = "postgresql://fastreact:fastreact@localhost:5432/fastreact"

settings = Settings()