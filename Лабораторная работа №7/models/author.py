class Author:
    """Класс, описывающий автора работы."""

    def __init__(self, name: str, group: str):
        """
        Создание нового автора.

        :param name: Имя автора
        :param group: Учебная группа
        """
        self._name = name
        self._group = group

    @property
    def name(self) -> str:
        """Получить имя автора."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Установить имя автора."""
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        self._name = value

    @property
    def group(self) -> str:
        """Получить группу автора."""
        return self._group
