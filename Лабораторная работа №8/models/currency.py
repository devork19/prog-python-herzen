"""Модуль, содержащий описание модели валюты."""

class Currency:
    """Класс, описывающий сущность валюты.

    Содержит основные атрибуты валюты, такие как цифровой код,
    символьный код, имя, номинал и текущий курс.
    """

    def __init__(self, num_code: str, char_code: str, name: str, value: float, nominal: int):
        """Инициализировать экземпляр Currency.

        Args:
            num_code (str): Цифровой код валюты (ISO 4217).
            char_code (str): Символьный код валюты (ISO 4217).
            name (str): Название валюты.
            value (float): Текущий курс валюты.
            nominal (int): Номинал (единиц валюты).
        """
        self._num_code = num_code
        self._char_code = char_code.upper()
        self._name = name
        self._value = value
        self._nominal = nominal

    @property
    def num_code(self) -> str:
        """Вернуть цифровой код валюты."""
        return self._num_code

    @property
    def char_code(self) -> str:
        """Вернуть символьный код валюты."""
        return self._char_code

    @char_code.setter
    def char_code(self, val: str) -> None:
        """Установить символьный код валюты.

        Args:
            val (str): Новый символьный код (3 символа).

        Raises:
            ValueError: Если длина кода не равна 3 символам.
        """
        if len(val) != 3:
            raise ValueError("Код валюты должен состоять из 3 символов")
        self._char_code = val.upper()

    @property
    def name(self) -> str:
        """Вернуть название валюты."""
        return self._name

    @property
    def value(self) -> float:
        """Вернуть текущий курс валюты."""
        return self._value

    @value.setter
    def value(self, val: float) -> None:
        """Установить курс валюты.

        Args:
            val (float): Новое значение курса.

        Raises:
            ValueError: Если курс отрицательный.
        """
        if val < 0:
            raise ValueError("Курс валюты не может быть отрицательным")
        self._value = val

    @property
    def nominal(self) -> int:
        """Вернуть номинал валюты."""
        return self._nominal
