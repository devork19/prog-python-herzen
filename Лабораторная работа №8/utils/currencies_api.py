"""Модуль для получения актуальных курсов валют через API ЦБ РФ."""
import requests
from typing import List, Dict, Any
import xml.etree.ElementTree as ET


def get_currencies() -> List[Dict[str, Any]]:
    """Получить список валют с сайта ЦБ РФ (XML).

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о валютах.
    """
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Ошибка получения данных от ЦБ РФ")
            return []

        # Парсинг XML
        root = ET.fromstring(response.content)
        currencies = []

        for valute in root.findall('Valute'):
            num_code = valute.find('NumCode').text
            char_code = valute.find('CharCode').text
            name = valute.find('Name').text
            nominal = int(valute.find('Nominal').text)
            # Значение приходит с запятой (86,50), нужно заменить на точку
            value_str = valute.find('Value').text.replace(',', '.')
            value = float(value_str)

            currencies.append({
                "num_code": num_code,
                "char_code": char_code,
                "name": name,
                "value": value,
                "nominal": nominal
            })
        return currencies

    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return []
