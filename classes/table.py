from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

from classes.city_weather import engine

Base = declarative_base()

class City_weather_table(Base):
    __tablename__ = 'City_weather_data'
    id = Column(Integer, primary_key=True)
    city_name = Column(String(50))
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

