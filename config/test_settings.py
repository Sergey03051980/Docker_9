"""
Настройки для тестов (используем SQLite)
"""
from .settings import *

# Переопределяем базу данных для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Отключаем миграции для ускорения тестов
MIGRATION_MODULES = {
    'auth': None,
    'contenttypes': None,
    'sessions': None,
}

# Увеличиваем скорость тестов
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Отключаем кеширование
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Отключаем Celery для тестов
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
