class Currency:
    """Модель валюты."""

    def __init__(self, char_code: str, name: str, value: float, nominal: int = 1):
        """
        Инициализация валюты.

        :param char_code: Код валюты (например, USD)
        :param name: Название (Доллар США)
        :param value: Текущий курс
        :param nominal: Номинал (за сколько единиц)
        """
        self._char_code = char_code
        self._name = name
        self._value = value
        self._nominal = nominal

    @property
    def char_code(self) -> str:
        """Получить символьный код."""
        return self._char_code

    @property
    def name(self) -> str:
        """Получить название валюты."""
        return self._name

    @property
    def value(self) -> float:
        """Получить курс."""
        return self._value

    @property
    def nominal(self) -> int:
        """Получить номинал."""
        return self._nominal
