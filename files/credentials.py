import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sqlalchemy import URL
from confi import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SQL_USER, SQL_PASSWORD,SQL_HOST,SQL_DB

class Crdentials:

    """
        manage the access keys to spotify api and mysql db
    """

    def credentials_spotify(self, scope:list=['user-read-recently-played']):

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri=REDIRECT_URI,
                                                    scope=scope))
        return sp

    def credentials_mysql(self, engine:str):
        url_object = URL.create(
        engine,
        username=SQL_USER,
        password=SQL_PASSWORD, 
        host=SQL_HOST,
        database=SQL_DB,
)       
        return url_object