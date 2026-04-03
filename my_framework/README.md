# WSGI_ZPENR

Это учебный микрофреймворк на языке Python, построенный на стандарте **WSGI**. Он позволяет быстро создавать веб-приложения с поддержкой маршрутизации и обработки различных HTTP-методов.

🔗 **GitHub Repository:** https://github.com/zpenr/open_code/tree/wsgi/my_framework

📦 **TestPyPI Project:** https://test.pypi.org/project/wsgi-zpenr/

---

## 🛠 Установка

pip install -i https://test.pypi.org/simple/ wsgi-zpenr==0.1.1

## 🚀 Быстрый старт

1. Создание приложения
Инициализируйте класс App и определите маршруты с помощью декоратора @app.route:

```python
from app import App, render_template

app = App()

@app.route('/')
def index():
    return "<h1>Добро пожаловать!</h1>"

@app.route('/hello/<name>')
def greet(name):
    return f"Привет, {name}!"
```

2. Обработка POST-запросов
Вы можете принимать данные из форм, указав метод POST:

```python 
@app.route('/submit', request_method='POST')
def handle_form(**kwargs):
    username = kwargs.get('username')
    return f"Данные получены для: {username}"
```

3. Работа с исключениями
Фреймворк поддерживает кастомные ошибки, которые автоматически рендерят страницу error_page.html:

```python

from app import DBNotFound

@app.route('/item/<id>')
def get_item(id):
    if id != "1":
        raise DBNotFound("Товар не найден в базе данных")
    return "Товар найден!"
```

## 🖥 Запуск сервера
Используйте встроенный сервер Python wsgiref для локальной разработки:

```python 
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print("Сервер запущен на http://localhost:8000")
        httpd.serve_forever()
```

## ⚙️ Основные возможности

| Функция | Описание |
| :--- | :--- |
| **Роутинг** | Поддержка динамических путей через регулярные выражения (напр. `<id>`). |
| **Параметры** | Автоматический парсинг Query String (GET) и данных из тела запроса (POST). |
| **Шаблоны** | Интеграция с Jinja2 через функцию `render_template`. |
| **Редиректы** | Специальный класс `Redirect('/url')` для перенаправления пользователя. |
| **Статика** | Базовая поддержка CSS-файлов (определяется по наличию 'static' в пути). |

## 🧩 Логика работы (By-design)
Фреймворк спроектирован как Stateless приложение. Основные этапы обработки запроса:

1. WSGI Entry Point: Принимает environ и start_response от сервера.

2. Routing: Сопоставляет путь из запроса с зарегистрированными декоратором @app.route путями с помощью регулярных выражений.

3. Dependency Injection: Динамические части пути (например, <id>) автоматически передаются в функцию-обработчик как именованные аргументы.

4. Response: Формирует корректный итерируемый объект и заголовки ответа.