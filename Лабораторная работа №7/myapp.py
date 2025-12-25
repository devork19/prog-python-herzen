import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Импортируем наши контроллеры
from controllers.app_controller import index_controller, author_controller
from controllers.user_controller import user_list_controller, user_detail_controller
from controllers.currency_controller import currency_list_controller

# Настройка Jinja2
# Указываем папку templates относительно текущего файла
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml'])
)


class MyRequestHandler(BaseHTTPRequestHandler):
    """
    Класс обработки запросов.
    Реализует простую маршрутизацию без фреймворков.
    """

    def do_GET(self):
        """Обработка GET запросов."""
        # Разбираем URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)

        # Переменные для ответа
        response_body = ""
        status_code = 200
        content_type = "text/html; charset=utf-8"

        try:
            # Маршрутизация
            if path == "/":
                response_body = index_controller(env)

            elif path == "/author":
                response_body = author_controller(env)

            elif path == "/users":
                response_body = user_list_controller(env)

            elif path == "/user":
                # Получаем id из параметров ?id=1
                user_id_list = query.get('id')
                if user_id_list:
                    uid = int(user_id_list[0])
                    response_body = user_detail_controller(env, uid)
                else:
                    response_body = "Ошибка: не указан id"
                    status_code = 400

            elif path == "/currencies":
                response_body = currency_list_controller(env)

            else:
                response_body = "<h1>404 Not Found</h1><p>Страница не найдена</p>"
                status_code = 404

        except Exception as e:
            # Простая обработка ошибок сервера
            status_code = 500
            response_body = f"<h1>500 Error</h1><p>{e}</p>"
            print(f"Server error: {e}")

        # Отправка заголовков
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

        # Отправка тела ответа (надо кодировать строку в байты)
        if isinstance(response_body, str):
            self.wfile.write(response_body.encode('utf-8'))
        else:
            self.wfile.write(bytes(str(response_body), 'utf-8'))


def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    """Запуск сервера."""
    server_address = ('', port)
    print(f"Сервер запущен на порту {port}...")
    print(f"Перейдите по ссылке: http://localhost:{port}")
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Сервер остановлен.")


if __name__ == '__main__':
    run()
