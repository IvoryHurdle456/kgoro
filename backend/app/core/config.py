from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    # Celery/Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # JWT/Auth (even if you haven't wired auth routes yet, it's fine to keep)
    JWT_SECRET: str = "dev-change-me"
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        env_file_encoding="utf-8",
        extra="ignore",  # don't crash if .env has keys you haven't added yet
    )


settings = Settings()
