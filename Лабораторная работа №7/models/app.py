from .author import Author

class App:
    """Класс с информацией о приложении."""

    def __init__(self, name: str, version: str, author: Author):
        """
        Инициализация приложения.

        :param name: Название приложения
        :param version: Версия
        :param author: Объект автора
        """
        self._name = name
        self._version = version
        self._author = author

    @property
    def name(self) -> str:
        """Получить название приложения."""
        return self._name

    @property
    def version(self) -> str:
        """Получить версию приложения."""
        return self._version

    @property
    def author(self) -> Author:
        """Получить объект автора."""
        return self._author
