from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra='allow')

    LICHESS_TOKEN: str

    GOOGLE_PRIVATE_KEY: str
    GOOGLE_PRIVATE_KEY_ID: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_EMAIL: str
    GOOGLE_TOKEN_URI: str
    GOOGLE_SHEET_ID: str


settings = Settings()
