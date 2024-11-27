from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    MAIL_SERVER_IP: str
    MAIL_SERVER_PORT: str
    MAIL_SERVER_SSL: str
    MAIL_SERVER_TLS: str
    MAIL_LOGIN: str
    MAIL_PASSWORD: str
    DISCORD_WEBHOOK: str
    STYLE_COLOR: str
    PRODUCT_ID: str
    SHOE_SIZE: str
    NOTIFICATION_RECEIVER: str


config = Config()
