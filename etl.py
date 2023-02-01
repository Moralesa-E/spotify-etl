import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from user_sqlalchemy import User

class ETL:

    def extract(self,sp, date, limit: int =50):
        """
            extracts data from the spotify api, 
            unfortunately the api does not allow to return more than 50 data,
            and it does not allow to consult more than a few days ago from today
        """
        dt_s =  int(date.timestamp())*1000
        return sp.current_user_recently_played(limit=limit, after=dt_s)

    def transform(self, data: list=[]):

        """
            transforms the data obtained from the spotify api into a pandas dataframe,
            removing duplicate data and evaluating for null values. 
            Extracting: name, artist, album, duration in milliseconds, popularity and when it was listened to
        """
        dt_trans = []
        
        for item in data['items']:
            dt_trans.append(
                {
                    "name": item["track"]['name'],
                    "artist": item["track"]['artists'][0]["name"],
                    "album": item["track"]["album"]["name"],
                    "duration_ms": item["track"]["duration_ms"],
                    "popularity": item["track"]["popularity"],
                    "played_at": item["played_at"],
                }
            )
        
        df = pd.DataFrame(dt_trans)
        df = df.drop_duplicates()
        df["played_at"]=pd.to_datetime(df["played_at"])
        
        if df.isnull().values.any():
            raise Exception("Null values exist ")
        
        return df
        
    def load(self,data,sql_cred):
        engine = create_engine(sql_cred)
        data.to_sql("RecentTracks", con=engine, index=False, if_exists='append')
        #export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/

    def consult_sql_recent_tracks(self, sql_cred):
        engine = create_engine(sql_cred)
        Session = sessionmaker(bind=engine)
        session = Session()

        tracks = session.query(User).all()
        t_resulst = []
        for track in tracks:
            t_resulst.append(                {
                    "name": track.name,
                    "artist": track.artist,
                    "album": track.album,
                    "duration_ms": track.duration_ms,
                    "popularity": track.popularity,
                    "played_at": track.played_at
                })

        df = pd.DataFrame(t_resulst)

        return df
