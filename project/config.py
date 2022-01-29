from pydantic import BaseSettings

class Settings(BaseSettings):
    START_DT: str
    END_DT: str

settings = Settings()