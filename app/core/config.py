import os
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()

class Settings(BaseSettings):
    chroma_db_path: str = Field(..., env="CHROMA_DB_PATH")
    crate_db_host: str = Field(..., env="CRATE_DB_HOST")
    crate_db_user: str = Field(..., env="CRATE_DB_USER")
    crate_db_pass: str = Field(..., env="CRATE_DB_PASS")
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")
    redis_password: str = Field(..., env="REDIS_PASSWORD")
    ollama_base_url: str = Field(..., env="OLLAMA_BASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()