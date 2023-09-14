import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)


class BotConfig:
    token: str | None = os.getenv("BOT_TOKEN")


class DatabaseConfig:
    user: str | None = os.getenv("POSTGRES_USER", default="postgres")
    password: str | None = os.getenv("POSTGRES_PASSWORD", default="postgres")
    host: str | None = os.getenv("POSTGRES_HOST", default="database")
    port: str | None = os.getenv("POSTGRES_PORT", default=5432)
    name: str | None = os.getenv("POSTGRES_DB", default="postgres")
