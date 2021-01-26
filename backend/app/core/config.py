from databases.core import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")


PROJECT_NAME = "python-rpg-api"
VERSION = "1.0.0"
API_PREFIX = "/api"
MYSQL_USER_PY = config("MYSQL_USER_PY", cast=str, default="root")
MYSQL_PASSWORD_PY = config("MYSQL_PASSWORD_PY", cast=Secret)
MYSQL_SERVER = config("MYSQL_SERVER", cast=str, default="db")
MYSQL_PORT = config("MYSQL_PORT", cast=str, default="3306")
MYSQL_DATABASE = config("MYSQL_DATABASE", cast=str)
DATABASE_URL = config(
  "DATABASE_URL",
  cast=DatabaseURL,
  default=f"mysql://{MYSQL_USER_PY}:{MYSQL_PASSWORD_PY}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)