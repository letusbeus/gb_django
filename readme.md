Создаём виртуальное окружение в Windows
```
mkdir project
cd project
python -m venv .venv
```
Далее активируем виртуальное окружение, чтобы все дальнейшие действия
выполнялись внутри него.
```
venv\Scripts\activate # Windows
venv\Scripts\activate.ps1 # Windows PowerShell
```
Устанавливаем Django и обязательные компоненты
```
pip install django
```
Создание проекта с именем myproject (укажите свое)
```
django-admin startproject myproject 
```
Запуск сервера и проверка работоспособности
```
# запуск сервера по умолчанию
python manage.py runserver 

# запуск с указанием порта
python manage.py runserver 8080 

# запуск с указанием IP-адреса и порта
python manage.py runserver 0.0.0.0:8080 
```
Создание приложения с именем myapp (укажите свое)
``` 
python manage.py startapp myapp
```
Добавление созданного приложения myapp в проект (myproject/myproject/settings.py)
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```