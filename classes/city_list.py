#Создаем класс в котором отражаем перечень городов
class City_list():
    __city_list: list

    #Для создания класса нужно будет ввести первый город
    def __init__(self, first_city):
        self.__city_list = [first_city]

    #Создаем геттер для проверки листа с городами
    def city_check(self):
        return self.__city_list

    #Создаем функцию для добавления города в лист и исключаем повторения
    def add_city_to_list(self, city):
        try:
            self.__city_list.append(str(city))
            set(self.__city_list)
            list(self.__city_list)
            print(f"Текущий лист городов: {self.city_check()} ")
        except Exception as e:
            print(f'Не удалось выполнить операцию. Ошибка {e}')

    #Создаем функцию для удаления некорректных названий из листа
    def remove_city_from_list(self, city):
        try:
            for one_element in city:
                if one_element in self.__city_list:
                    self.__city_list.remove(city)
            else:
                print("Такого города нет в перечне, либо название введено неверно")
        except Exception as e:
            print(f'Не удалось выполнить операцию. Ошибка {e}')