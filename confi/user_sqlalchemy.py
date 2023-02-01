from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, BIGINT, TIMESTAMP

Base = declarative_base()

class User(Base):
    __tablename__ = 'recenttracks'
    
    name = Column(String)
    artist = Column(String)
    album = Column(String)
    duration_ms = Column(BIGINT)
    popularity = Column(BIGINT)
    played_at = Column(TIMESTAMP, primary_key=True)