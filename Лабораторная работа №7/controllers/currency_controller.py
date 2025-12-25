from utils.currencies_api import get_currencies


def currency_list_controller(env):
    """Контроллер списка валют."""
    # Получаем свежие данные через утилиту
    data = get_currencies()

    template = env.get_template("currencies.html")
    return template.render(
        currencies=data,
        title="Курсы валют"
    )
