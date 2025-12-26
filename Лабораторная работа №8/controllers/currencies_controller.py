"""Модуль бизнес-логики для управления валютами."""

from typing import List, Dict, Any
from controllers.database_controller import DatabaseController

class CurrenciesController:
    """Контроллер, отвечающий за обработку действий с валютами."""

    def __init__(self, db_controller: DatabaseController):
        """Инициализировать контроллер валют.

        Args:
            db_controller (DatabaseController): Экземпляр контроллера БД.
        """
        self.db = db_controller

    def get_currencies_list(self) -> List[Dict[str, Any]]:
        """Получить подготовленный список валют для отображения.

        Returns:
            List[Dict[str, Any]]: Список валют.
        """
        return self.db.get_all_currencies()

    def delete_currency_by_id(self, currency_id: int) -> None:
        """Удалить валюту, используя механизм БД.

        Args:
            currency_id (int): ID удаляемой валюты.
        """
        self.db.delete_currency(currency_id)

    def update_rate(self, char_code: str, value: float) -> None:
        """Обновить курс валюты.

        Args:
            char_code (str): Символьный код.
            value (float): Новое значение.
        """
        self.db.update_currency_rate(char_code, value)
