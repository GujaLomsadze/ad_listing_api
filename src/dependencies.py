import jwt
import psycopg2
from fastapi import Header, HTTPException

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHM = "HS256"


def decode(token):
    striped_token = token.replace("Bearer ", "")

    db = get_db()

    with db.cursor() as curs:
        curs.execute(f"select owner from tokens where token = '{striped_token}'")

        data = curs.fetchall()
        print(data)
        if data or data != []:
            return True
        else:
            return False


def get_db():
    connection = psycopg2.connect(
        host="localhost",
        database="ads",
        user="postgres",
        password="adminD4761#guja"
    )
    return connection


async def get_token_header(Authorization: str = Header(...)):
    token_status = decode(Authorization)
    if not token_status:
        raise HTTPException(status_code=401, detail="Token is not valid nigger!")

    # TODO: Validate token from database
