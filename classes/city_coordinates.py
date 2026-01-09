import requests
from classes.city_list import City_list
import config.global_config

class City_location():
    __city_lat: float
    __city_lon: float

    def __init__(self, lat, lon):
        self.__city_lat = lat
        self.__city_lon = lon

    def location_check(self):
        return self.__city_lat, self.__city_lon
