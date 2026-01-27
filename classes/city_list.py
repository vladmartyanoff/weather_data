import json
import requests
import config.global_config
from config.global_config import URL_city_to_location
import logging

logger = logging.getLogger("classes.city_list")


#Создаем класс в котором отражаем перечень городов
class City_list():
    __city_list: list
    __city_location: dict
    __state_code: str
    __country_code: str
    __limit: str
    list_of_cities_with_locations: list

    #Для создания класса нужно будет ввести первый город
    def __init__(self, first_city):
        self.__API_key = config.global_config.API_key
        self.__state_code = config.global_config.state_code
        self.__country_code = config.global_config.country_code
        self.__limit = config.global_config.limit
        self.__city_list = [first_city]
        self.__list_of_cities_with_locations = []

    #Создаем геттер для проверки листа с городами
    def city_check(self):
        return self.__city_list


    #Создаем функцию для добавления города в лист и исключаем повторения
    def add_city_to_list(self, city):
        try:
            self.__city_list.append(str(city))
            set(self.__city_list)
            list(self.__city_list)
            logger.info(f"Город успешно добавлен. Текущий лист городов: {self.city_check()} ")
        except Exception as e:
            logger.info(f'Не удалось выполнить операцию. Ошибка {e}')

    #Создаем функцию для удаления некорректных названий из листа
    def remove_city_from_list(self, city):
        try:
            for one_element in city:
                if one_element in self.__city_list:
                    self.__city_list.remove(city)
            else:
                logger.info("Такого города нет в перечне, либо название введено неверно")
        except Exception as e:
            logger.info(f'Не удалось выполнить операцию. Ошибка {e}')

    # Создаем функцию для получения словаря - город, координаты и добавления его в лист словарей
    def dict_fullfill(self):
        # Запускаем цикл обработки листа с названиями городов, для каждого создаем свой словарь чтобы дальше было проще обрабатывать
        for one_element in self.__city_list:
            __city_location = {
                "city_name": str(one_element),
                "city_lat": "",
                "city_lon": ""
            }
            # Делаем запрос к API
            try:
                city_name = str(one_element)
                r = requests.get(url= f'{URL_city_to_location}direct?q={city_name},{self.__state_code},{self.__country_code}&limit={self.__limit}&appid={self.__API_key}')
                request_result = r.json()
                # В случае успешного ответа присваиваем полученные значения ключам в словаре
                if r.status_code == 200:
                    lat = request_result[0]['lat']
                    lon = request_result[0]['lon']
                    __city_location["city_lat"] = str(lat)
                    __city_location["city_lon"] = str(lon)
                    logger.info(f"Координаты города {city_name} = {lat}; {lon}")
                    logger.info(__city_location)
                    # Добавляем словарь с городом в общий лист
                    self.__list_of_cities_with_locations.append(__city_location)
            except Exception as e:
                logger.info(f'Не удалось выполнить операцию. Ошибка {e}')
        try:
            # Записываем полученный лист со словарями во внешний джисон-файл
            with open(r"C:\Users\Vlad\PycharmProjects\weather_data\config\cities_locations.json", 'w',
                      encoding="utf-8") as cl:
                json.dump(self.__list_of_cities_with_locations, cl, ensure_ascii = False, indent = 2) #Indent - отступы для удобного чтения
                logger.info("Данные сохранены в cities_locations.json")
        except Exception as e:
            logger.info(f'Не удалось выполнить операцию. Ошибка {e}')

