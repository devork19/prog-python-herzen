from models.author import Author
from models.app import App

# Создаем объекты один раз (здесь указываем твои данные)
my_author = Author("Стажков Данила", "ИВТ 2-1")
my_app = App("CurrencyChecker", "1.0 Beta", my_author)

def index_controller(env):
    """Контроллер главной страницы."""
    template = env.get_template("index.html")
    # Рендерим шаблон
    return template.render(
        app=my_app,
        title="Главная"
    )

def author_controller(env):
    """Контроллер страницы об авторе."""
    # Используем тот же шаблон index, просто передаем флаг
    template = env.get_template("index.html")
    return template.render(
        app=my_app,
        title="Об авторе",
        show_author=True
    )
