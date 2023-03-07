from starlette.config import Config

from starlette.datastructures import CommaSeparatedStrings, Secret

###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = ""

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
