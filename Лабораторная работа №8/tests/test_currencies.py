"""Модуль модульного тестирования контроллеров."""

import unittest
from unittest.mock import MagicMock
from controllers.currencies_controller import CurrenciesController


class TestCurrenciesController(unittest.TestCase):
    """Тесты для CurrenciesController."""

    def setUp(self):
        """Подготовить окружение перед каждым тестом."""
        self.mock_db = MagicMock()
        self.controller = CurrenciesController(self.mock_db)

    def test_list_currencies(self):
        """Тест получения списка валют."""
        # Настройка mock-объекта
        expected_data = [{"id": 1, "char_code": "USD", "value": 90.5}]
        self.mock_db.get_all_currencies.return_value = expected_data

        # Вызов метода
        result = self.controller.get_currencies_list()

        # Проверки
        self.assertEqual(result, expected_data)
        self.assertEqual(result[0]['char_code'], "USD")
        self.mock_db.get_all_currencies.assert_called_once()

    def test_update_currency(self):
        """Тест вызова обновления валюты."""
        self.controller.update_rate("EUR", 100.0)

        # Проверяем, что метод БД был вызван с правильными аргументами
        self.mock_db.update_currency_rate.assert_called_once_with("EUR", 100.0)


if __name__ == '__main__':
    unittest.main()
