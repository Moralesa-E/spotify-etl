from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
REDIRECT_URI = config('REDIRECT_URI')
SQL_USER = config("SQL_USER")
SQL_PASSWORD = config("SQL_PASSWORD")
SQL_HOST = config("SQL_HOST")
SQL_DB = config("SQL_DB")