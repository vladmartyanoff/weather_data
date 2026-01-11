import classes.city_list
import requests
import classes.fullfilled_list
import config.global_config
from classes.city_list import City_list
from config.global_config import URL_city_to_location, city_name, state_code, country_code, limit, API_key

list_1 = City_list("Moscow")
list_1.add_city_to_list("Prague")
list_1.city_check()
list_1.dict_fullfill()
list_1.location_check()


