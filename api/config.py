from pydantic import BaseSettings

class Settings(BaseSettings):
    ROOT_URL: str

settings = Settings()