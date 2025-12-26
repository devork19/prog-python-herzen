"""Главный модуль приложения. Запускает HTTP-сервер."""

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader

from controllers.database_controller import DatabaseController
from controllers.currencies_controller import CurrenciesController

# Инициализация окружения
DB = DatabaseController()
CURRENCY_CTRL = CurrenciesController(DB)
TEMPLATE_ENV = Environment(loader=FileSystemLoader('templates'))


class MyRequestHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов."""

    def do_GET(self):
        """Обработать GET-запрос и маршрутизировать его."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)

        if path == '/':
            self._render_template('index.html', title="Главная")

        elif path == '/currencies':
            currencies = CURRENCY_CTRL.get_currencies_list()
            self._render_template('currencies.html', currencies=currencies)

        elif path == '/currency/delete':
            # Пример: /currency/delete?id=1
            c_id = query.get('id', [None])[0]
            if c_id:
                CURRENCY_CTRL.delete_currency_by_id(int(c_id))
            # Редирект обратно на список
            self._redirect('/currencies')

        elif path == '/currency/update':
            # Пример: /currency/update?USD=100.0
            for key, value in query.items():
                # Простая логика: ключ запроса считается кодом валюты
                try:
                    new_val = float(value[0])
                    CURRENCY_CTRL.update_rate(key, new_val)
                except ValueError:
                    pass
            self._redirect('/currencies')

        else:
            self.send_error(404, "Page Not Found")

    def _render_template(self, template_name: str, **kwargs):
        """Рендеринг HTML шаблона Jinja2."""
        try:
            template = TEMPLATE_ENV.get_template(template_name)
            content = template.render(**kwargs)
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except Exception as e:
            self.send_error(500, f"Template Error: {e}")

    def _redirect(self, location: str):
        """Выполнить HTTP редирект."""
        self.send_response(303)
        self.send_header('Location', location)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    """Запустить сервер."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Запуск сервера на порту {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    run()
