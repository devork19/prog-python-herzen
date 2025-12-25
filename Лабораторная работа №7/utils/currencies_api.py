import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import List, Dict, Any


def get_currencies() -> List[Dict[str, Any]]:
    """
    Получает актуальные курсы валют с сайта ЦБ РФ.

    Парсит XML и возвращает список словарей.
    """
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    try:
        with urllib.request.urlopen(url) as response:
            xml_content = response.read()

        root = ET.fromstring(xml_content)
        result = []

        for valute in root.findall('Valute'):
            # Нам нужны только основные валюты для примера
            char_code = valute.find('CharCode').text
            if char_code not in ['USD', 'EUR', 'CNY', 'GBP']:
                continue

            # ЦБ отдает числа с запятой, меняем на точку
            val_str = valute.find('Value').text.replace(',', '.')

            currency_data = {
                'char_code': char_code,
                'name': valute.find('Name').text,
                'nominal': int(valute.find('Nominal').text),
                'value': float(val_str)
            }
            result.append(currency_data)
        return result
    except Exception as e:
        print(f"Ошибка при загрузке курсов: {e}")
        return []


def get_history(currency_code: str, days: int = 90) -> Dict[str, list]:
    """
    Получает историю котировок для графика.

    Для упрощения используем заранее известные ID для основных валют,
    так как API ЦБ требует внутренний ID (R01235 и т.д.), а не CharCode.
    """
    # Хардкод ID для примера, так как поиск ID это отдельный запрос
    cbr_ids = {
        'USD': 'R01235',
        'EUR': 'R01239',
        'CNY': 'R01375',
        'GBP': 'R01035'
    }

    if currency_code not in cbr_ids:
        return {'labels': [], 'data': []}

    val_id = cbr_ids[currency_code]
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    # Формат даты для ЦБ: dd/mm/yyyy
    d1 = start_date.strftime("%d/%m/%Y")
    d2 = end_date.strftime("%d/%m/%Y")

    url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={d1}&date_req2={d2}&VAL_NM_RQ={val_id}"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()

        root = ET.fromstring(data)
        labels = []
        values = []

        for record in root.findall('Record'):
            date_str = record.get('Date')
            val = float(record.find('Value').text.replace(',', '.'))
            labels.append(date_str)
            values.append(val)

        return {'labels': labels, 'data': values}
    except Exception as e:
        print(f"Ошибка истории: {e}")
        return {'labels': [], 'data': []}
