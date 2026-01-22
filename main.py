from classes.city_weather import City_weather
from config.logging_config import setup_logging

setup_logging()

test = City_weather()
test.list_filling()
test.weather_check()




