from pydantic import BaseSettings
from sqlalchemy.ect.declarative import declarative_base
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:8000/etscursos'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True
        
settings = Settings()