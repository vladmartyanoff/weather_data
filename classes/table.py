from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


Base = declarative_base()

class City_weather_table(Base):
    __tablename__ = 'city_weather_data'
    id = Column(Integer, primary_key=True)
    city_name = Column(String(50))
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow())

