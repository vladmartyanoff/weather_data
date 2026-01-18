import json
import datetime
import config.global_config
from config.global_config import URL_weather_check
import requests


class City_weather():
    __list_of_cities_with_locations: list
    __API_key: str
    __lat: str
    __lon: str
    __city_name: str
    __filename: str

    def __init__(self):
        self.__list_of_cities_with_locations = []
        self.__API_key = ""
        self.__lat = ""
        self.__lon = ""
        self.__city_name = ""
        self.__filename = ""

    def list_filling(self, __filename = r"C:\Users\Vlad\PycharmProjects\weather_data\config\cities_locations.json"):
        try:
            with open(__filename, "r", encoding= "utf-8") as file:
                self.__list_of_cities_with_locations = json.load(file)
                print(f"Лист заполнен успешно:{self.__list_of_cities_with_locations} ")
                element_count = len(self.__list_of_cities_with_locations)
                print(f"Количество элементов в листе = {element_count}")
        except Exception as e:
            print(e)

    def weather_check(self):
        if len(self.__list_of_cities_with_locations) > 0:
            for one_element in self.__list_of_cities_with_locations:
                try:
                    self.__API_key = config.global_config.API_key
                    self.__lat = one_element.get("city_lat")
                    self.__lon = one_element.get("city_lon")
                    self.__city_name = one_element.get("city_name")
                    r = requests.get (url= f"{URL_weather_check}weather?lat={self.__lat}&lon={self.__lon}&appid={self.__API_key}")
                    request_result = r.json()
                    if r.status_code == 200:
                        weather = request_result["main"]
                        temp = float(weather["temp"]) - 273.15
                        rounded_temp = round(temp, 2)
                        pressure = weather["pressure"]
                        humidity = weather["humidity"]
                        current_date_time = datetime.datetime.now().isoformat(timespec='seconds')
                        print(f' {current_date_time} -- В городе {self.__city_name} температура воздуха {rounded_temp}C°, атмосферное давление - {pressure} Па, влажность воздуха - {humidity}%')
                except Exception as e:
                    print(e)
        else:
            print("Словарь пуст")



