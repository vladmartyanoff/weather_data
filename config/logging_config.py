import logging
import os

#Задаем параметры логирования
LOGGING_CONFIG = {
    #Версия схемы (обязательно единица иначе падает в ошибку - не знаю почему)
    'version': 1,

    # Существующие логеры не отключаем
    'disable_existing_loggers': False,

    # Создаем шаблон сообщений
    'formatters': {
        'detailed': {
            'format': # "asctime" - время запроса, "levelname" - уровень (инфо\дебаг\ошибка), "name" - в каком файле ошибка, "lineno" - номер строки в коде, "message" - текст лога
                '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s'
        }
    },

    # Задаем направления вывода сообщений
    'handlers': {

        # Вывод в консоль для быстрого доступа
        'console': {

            # Вывод в консоль
            'class': 'logging.StreamHandler',
            # Вывод сообщений не ниже уровня INFO
            'level': 'INFO',
            # Вывод сообщений в формате "detailed" который указали выше
            'formatter': 'detailed'
        },

        # Вывод во внешний файл
        'file': {

            # Вывод во внешний файл
            'class': 'logging.FileHandler',
            # Путь к файлу и название
            'filename': os.path.join(os.path.dirname(__file__), '../logs/app.log'),
            # Тип "а" - добавление записей ("w" - перезапись)
            'mode': 'a',
            # Вывод сообщений на русском языке
            'encoding': 'utf-8',
            # Вывод сообщений не ниже уровня "DEBUG"
            'level': 'DEBUG',
            # Вывод сообщений в формате "detailed" который указали выше
            'formatter': 'detailed'
        }
    },
    # Привязываем логи к рабочим файлам
    'loggers': {
        # Параметры для файла "city_weather"
        'city_weather': {
            # Вывод сообщений не ниже уровня "DEBUG"
            'level': 'DEBUG',
            # Вывод и в консоль и в файл
            'handlers': ['console', 'file'],
            # Не передавать выше (чтобы не дублировалось)
            'propagate': False
        },
        # Параметры для файла "main"
        'main': {
            # Вывод сообщений не ниже уровня "INFO"
            'level': 'INFO',
            # Вывод и в консоль и в файл
            'handlers': ['console', 'file']
        },
        # Параметры для файла "city_weather"
        'city_list': {
            # Вывод сообщений не ниже уровня "DEBUG"
            'level': 'DEBUG',
            # Вывод и в консоль и в файл
            'handlers': ['console', 'file'],
            # Не передавать выше (чтобы не дублировалось)
            'propagate': False
        }
    }
}

def setup_logging():
    #Инициализация логирования
    logging.config.dictConfig(LOGGING_CONFIG)
