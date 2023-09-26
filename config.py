from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    server_port: int
    redis_host: str
    redis_port: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
