import json
import datetime
import config.global_config
from config.global_config import URL_weather_check
import requests
import pandas as pd
import re
import os
import logging

#Задаем логирование для класса
logger = logging.getLogger("classes.city_weather")

#Создаем класс
class City_weather():
    __list_of_cities_with_locations: list
    __API_key: str
    __lat: str
    __lon: str
    __city_name: str
    __filename: str
    __weather_list: list

    # Задаем начальные значения переменных класса
    def __init__(self):
        self.__list_of_cities_with_locations = []
        self.__API_key = ""
        self.__lat = ""
        self.__lon = ""
        self.__city_name = ""
        self.__filename = ""
        self.__weather_list = []

    # Создаем функцию заполнения листа с координатами городов из файла
    def list_filling(self, __filename = os.path.join(os.path.dirname(__file__), '../config/cities_locations.json')):
        try:
            with open(__filename, "r", encoding= "utf-8") as file:
                self.__list_of_cities_with_locations = json.load(file)
                logger.info(f"Лист заполнен успешно:{self.__list_of_cities_with_locations} ")
                element_count = len(self.__list_of_cities_with_locations)
                logger.info(f"Количество элементов в листе = {element_count}")
        except Exception as e:
            logger.error(e)

    # Создаем функцию для проверки погоды для городов в листе
    def weather_check(self):
        # Задаем директорию куда будем выгружать результаты
        project_root = os.path.dirname(os.path.dirname(__file__))
        results_directory = os.path.join(project_root, "results")
        # Проверяем существует ли директория, если не существует то будет создаваться
        os.makedirs(results_directory, exist_ok=True)
        try:
            # Проверяем есть ли значения в листе
            if len(self.__list_of_cities_with_locations) > 0:
                # Обнуляем лист класса перед началом работы
                self.__weather_list = []
                # Делаем запрос на текущее время
                current_date_time = str(datetime.datetime.now().isoformat(timespec='seconds'))
                # Заменяем ":" в строке времени на "-" поскольку в их нельзя использовать в Windows
                safe_filename = re.sub(r'[:/]', "-", current_date_time)
                # Начинаем цил обработки значений из листа
                for one_element in self.__list_of_cities_with_locations:
                    __city_weather_dict = {
                        "city_name": "",
                        "temperature": "",
                        "pressure": "",
                        "humidity": ""
                    }
                    try:
                        self.__API_key = config.global_config.API_key
                        self.__lat = one_element.get("city_lat")
                        self.__lon = one_element.get("city_lon")
                        self.__city_name = one_element.get("city_name")
                        # Делаем запрос к API
                        r = requests.get (url= f"{URL_weather_check}weather?lat={self.__lat}&lon={self.__lon}&appid={self.__API_key}")
                        request_result = r.json()
                        # Если ответ удовлетворительный записываем значения в пустой словарь
                        if r.status_code == 200:
                            # Извлекаем значение температуры
                            weather = request_result["main"]
                            temp = float(weather["temp"]) - 273.15
                            rounded_temp = round(temp, 2)
                            __city_weather_dict["city_name"] = one_element.get("city_name")
                            __city_weather_dict["temperature"] = str(rounded_temp)
                            # Извлекаем значение давления
                            pressure = weather["pressure"]
                            __city_weather_dict["pressure"] = str(pressure)
                            # Извлекаем значение влажности воздуха
                            humidity = weather["humidity"]
                            __city_weather_dict["humidity"] = str(humidity)
                            # Подтверждаем выполнение
                            logger.info(f' {current_date_time} -- В городе {self.__city_name} температура воздуха {rounded_temp}C°, атмосферное давление - {pressure} Па, влажность воздуха - {humidity}%')
                            # Добавляем значения в итоговый лист словарей
                            self.__weather_list.append(__city_weather_dict)
                    # Обрабатываем исключения
                    except Exception as api_e:
                        logger.error(f"Ошибка API:{api_e}")
                # Задаем путь для записис CSV файла
                csv_filename = f"weather_{safe_filename}.csv"
                csv_path = os.path.join(results_directory, csv_filename)
                # Переводим лист в датафрейм
                data_framed_list = pd.DataFrame(self.__weather_list)
                # Записываем файл и отчитываемся о выполнении
                data_framed_list.to_csv(csv_path, index = False, encoding="utf-8")
                logger.info(f"Файл успешно сохранен в {csv_path}")
            else:
                logger.error("Словарь пуст")
        except Exception as e:
            logger.error(f"Ошибка: {e}")



