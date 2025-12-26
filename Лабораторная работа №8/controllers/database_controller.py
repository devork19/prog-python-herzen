"""Модуль для взаимодействия с базой данных SQLite."""

import sqlite3
from typing import List, Dict, Any, Optional


# Если вы добавили requests, то раскомментируйте следующую строку:
# from utils.currencies_api import get_currencies

class DatabaseController:
    """Контроллер для управления соединением с БД и выполнения SQL-запросов."""

    def __init__(self):
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()
        self._seed_data()

    def _create_tables(self) -> None:
        script = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS currency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_code TEXT NOT NULL,
            char_code TEXT NOT NULL,
            name TEXT NOT NULL,
            value FLOAT,
            nominal INTEGER
        );
        CREATE TABLE IF NOT EXISTS user_currency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            currency_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(currency_id) REFERENCES currency(id)
        );
        """
        self.cursor.executescript(script)
        self.conn.commit()

    def _seed_data(self) -> None:
        # Если используете requests:
        # currencies = get_currencies()
        # Если пока без requests (как в первом варианте):
        currencies = [
            ("840", "USD", "Доллар США", 90.50, 1),
            ("978", "EUR", "Евро", 98.10, 1),
        ]

        # ЛОГИКА ВСТАВКИ (должна быть адаптирована под то, что возвращает get_currencies или список выше)
        # Для простого списка кортежей (как в примере выше):
        self.cursor.executemany(
            "INSERT INTO currency(num_code, char_code, name, value, nominal) VALUES(?, ?, ?, ?, ?)",
            currencies
        )
        self.conn.commit()

    def get_all_currencies(self) -> List[Dict[str, Any]]:
        self.cursor.execute("SELECT * FROM currency")
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def delete_currency(self, currency_id: int) -> None:
        sql = "DELETE FROM currency WHERE id = ?"
        self.cursor.execute(sql, (currency_id,))
        self.conn.commit()

    def update_currency_rate(self, char_code: str, new_value: float) -> None:
        sql = "UPDATE currency SET value = ? WHERE char_code = ?"
        self.cursor.execute(sql, (new_value, char_code))
        self.conn.commit()
