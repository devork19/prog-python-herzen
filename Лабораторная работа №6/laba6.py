import requests
import sys
def get_currencies_v1(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Первая версия функции — просто пробуем получить курсы валют.
    Если что-то не так, пишем сообщение в консоль.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "Valute" not in data:
            print("Ошибка: в ответе нет данных о валютах", file=sys.stdout)
            return None

        valutes = data["Valute"]
        result = {}
        for code in currency_codes:
            if code in valutes:
                result[code] = valutes[code]["Value"]
            else:
                print(f"Ошибка: валюты {code} нет в ответе", file=sys.stdout)

        return result

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к API: {e}", file=sys.stdout)
        return None
# итерация 2 добавляем декоратор для логирования ошибок
from functools import wraps
def log_errors(func):
    """
    Декоратор, который перехватывает ошибки и выводит их в консоль.
    Это нужно, чтобы не писать try-except внутри каждой функции.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса к API: {e}", file=sys.stdout)
            return None
        except KeyError as e:
            print(f"Ошибка данных, нет ключа {e}", file=sys.stdout)
            return None
        except Exception as e:
            print(f"Неизвестная ошибка: {e}", file=sys.stdout)
            return None

    return wrapper
@log_errors
def get_currencies_v2(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Вторая версия функции — теперь с декоратором log_errors.
    """
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if "Valute" not in data:
        raise KeyError("Valute")

    valutes = data["Valute"]
    result = {code: valutes[code]["Value"] for code in currency_codes if code in valutes}
    # проверяем, все ли валюты найдены
    missing = [c for c in currency_codes if c not in valutes]
    if missing:
        raise KeyError(f"Отсутствуют валюты: {', '.join(missing)}")
    return result
# итерация 3 используем модуль logging для красивого вывода
import logging
# настраиваем логирование (будет выводить время, уровень и сообщение)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()]  # вывод в консоль
)
logger = logging.getLogger(__name__)
def log_errors_v3(func):
    """
    Декоратор для логирования ошибок через модуль logging.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка запроса к API: {e}")
            return None
        except KeyError as e:
            logger.error(f"Ошибка данных: нет ключа {e}")
            return None
        except Exception as e:
            logger.exception("Неизвестная ошибка")
            return None
    return wrapper
@log_errors_v3
def get_currencies_v3(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Третья версия функции — с использованием logging.
    """
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if "Valute" not in data:
        raise KeyError("Valute")
    valutes = data["Valute"]
    result = {code: valutes[code]["Value"] for code in currency_codes if code in valutes}
    missing = [c for c in currency_codes if c not in valutes]
    if missing:
        raise KeyError(f"Нет таких валют: {', '.join(missing)}")
    return result
# пример, как это работает
if __name__ == "__main__":
    print(" итерация 1")
    print(get_currencies_v1(["USD", "EUR", "GBP"]))
    print("\n итерация 2")
    print(get_currencies_v2(["USD", "EUR", "GBP"]))
    print("\n итерация 3 ")
    print(get_currencies_v3(["USD", "EUR", "GBP"]))