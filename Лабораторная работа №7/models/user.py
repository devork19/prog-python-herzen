class User:
    """Модель пользователя системы."""

    def __init__(self, user_id: int, name: str):
        """
        Создать пользователя.

        :param user_id: Уникальный ID
        :param name: Имя пользователя
        """
        self._id = user_id
        self._name = name

    @property
    def id(self) -> int:
        """Получить ID пользователя."""
        return self._id

    @property
    def name(self) -> str:
        """Получить имя."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Установить имя с проверкой типа."""
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        self._name = value
