class UserCurrency:
    """
    Промежуточная модель для связи пользователя и валюты.
    Показывает, на что подписан пользователь.
    """

    def __init__(self, user_id: int, currency_code: str):
        """
        Создать подписку.

        :param user_id: ID пользователя
        :param currency_code: Код валюты (USD, EUR)
        """
        self.user_id = user_id
        self.currency_code = currency_code
