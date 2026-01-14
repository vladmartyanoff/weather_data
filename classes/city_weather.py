import json

class City_weather():
    __list_of_cities_with_locations: list
    __API_key: str
    __lat: str
    __lon: str
    __filename: str

    def __init__(self):
        self.__list_of_cities_with_locations = []
        self.__API_key = ""
        self.__lat = ""
        self.__lon = ""
        self.__filename = ""

    def list_filling(self, __filename = r"C:\Users\Vlad\PycharmProjects\weather_data\config\cities_locations.json"):
        try:
            with open(__filename, "r", encoding= "utf-8") as file:
                self.__list_of_cities_with_locations = json.load(file)
                print(f"Лист заполнен успешно:{self.__list_of_cities_with_locations} ")
        except Exception as e:
            print(e)