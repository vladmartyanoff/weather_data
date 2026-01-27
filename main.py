from classes.city_list import City_list
from classes.city_weather import City_weather
from config.logging_config import setup_logging
import logging

setup_logging()
logging.info("Старт программы")

#Добавлены города: Москва, Дублин, Токио, Лондон, Вашингтон
city_list = City_list("Moscow")
city_list.add_city_to_list("Dublin")
city_list.add_city_to_list("Tokio")
city_list.add_city_to_list("London")
city_list.add_city_to_list("Washington")
city_list.dict_fullfill()

#Проверяем погоду в городах из листа  !!ОБЯЗАТЕЛЬНО СО СКОБКАМИ - СКОБКИ СОЗДАЮТ ЭКЗЕМПЛЯР КЛАССА!!
weather_check = City_weather()
weather_check.list_filling()
weather_check.weather_check()






