import jwt
import psycopg2
from fastapi import Header

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHM = "HS256"


def decode(token):
    striped_token = token.replace("Bearer ", "")
    payload = jwt.decode(striped_token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload


def get_db():
    connection = psycopg2.connect(
        host="localhost",
        database="ads",
        user="postgres",
        password="adminD4761#guja"
    )
    yield connection
    connection.close()


async def get_token_header(x_token: str = Header(...)):
    payload = decode(x_token)

    return payload

    # TODO: Validate token from database
