import json
from models.user import User
from utils.currencies_api import get_history

# Имитация базы данных (список пользователей)
users_db = [
    User(1, "Алексей Петров"),
    User(2, "Мария Сидорова"),
    User(3, "Тестовый Юзер")
]

# Имитация подписок (UserCurrency)
# ID пользователя -> Список кодов валют
subscriptions = {
    1: ['USD', 'EUR'],
    2: ['CNY'],
    3: ['GBP', 'USD']
}


def user_list_controller(env):
    """Показать всех пользователей."""
    template = env.get_template("users.html")
    return template.render(
        users=users_db,
        title="Пользователи"
    )


def user_detail_controller(env, user_id):
    """
    Показать профиль пользователя и графики.
    Сюда добавлена логика самостоятельной работы.
    """
    # Ищем пользователя в списке
    user = None
    for u in users_db:
        if u.id == user_id:
            user = u
            break

    if not user:
        return "Пользователь не найден"

    # Получаем подписки
    user_subs = subscriptions.get(user.id, [])

    # Готовим данные для графиков
    charts = []
    for code in user_subs:
        history = get_history(code)
        charts.append({
            'code': code,
            'labels': json.dumps(history['labels']),  # JSON для JS
            'data': json.dumps(history['data'])
        })

    template = env.get_template("user_detail.html")
    return template.render(
        user=user,
        charts=charts,
        title=f"Профиль {user.name}"
    )
