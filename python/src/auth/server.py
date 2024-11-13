import datetime
import jwt
import os
import psycopg2
from flask import Flask, request


server = Flask(__name__)
url = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(url)


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    query = "SELECT email, password FROM public.user WHERE email=%s"
    cursor = connection.cursor()
    res = cursor.execute(query, (auth.username,))

    if res > 0:
        user = cursor.fetchone()
        email = user[0]
        password = user[1]

        if auth.username != email and auth.password != password:
            return "invalid credentials", 401
        else:
            create_jwt(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "invalid creadentials", 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]
    if not encoded_jwt:
        return "missing credentials", 401

    try:
        token = encoded_jwt.split(" ")[1]
        decoded_jwt = jwt.decode(
            token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])
    except Exception:
        return "not authorized", 403
    return decoded_jwt, 200


def create_jwt(username, secret, is_admin):
    exp_time = datetime.datetime.now(tz=datetime.datetime.utc)\
        + datetime.timedelta(days=1)
    iat = datetime.datetime.now(tz=datetime.datetime.utc)
    return jwt.encode(
        {"username": username,
         "exp": exp_time,
         "iat": iat,
         "admin": is_admin},
        secret, algorithm="HS256")
