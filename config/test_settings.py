"""
Test settings for CI/CD pipeline
"""
import os
from .settings import *

# Используем SQLite для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# ОТКЛЮЧАЕМ создание разрешений через отключение миграций
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Отключаем кеширование для тестов
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Отключаем Celery для тестов
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Быстрые хэшеры для тестов
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Отключаем отладку
DEBUG = False

# Тестовый секретный ключ
SECRET_KEY = 'test-secret-key-for-ci-cd-pipeline'

# Разрешаем все хосты для тестов
ALLOWED_HOSTS = ['*']
