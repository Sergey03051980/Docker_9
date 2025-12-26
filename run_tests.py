#!/usr/bin/env python
"""
Скрипт для запуска тестов с SQLite
"""
import os
import sys
import django

# Устанавливаем тестовые настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.test_settings')

def setup_django():
    """Настройка Django для тестов"""
    try:
        django.setup()
        print("✅ Django настроен для тестов")
        return True
    except Exception as e:
        print(f"❌ Ошибка настройки Django: {e}")
        return False

def run_django_tests():
    """Запуск Django тестов"""
    from django.core.management import execute_from_command_line
    
    # Запускаем тесты
    execute_from_command_line(['manage.py', 'test', 'tests/'])

def main():
    """Главная функция"""
    print("🧪 Запуск тестов с SQLite...")
    
    if not setup_django():
        sys.exit(1)
    
    try:
        run_django_tests()
        print("✅ Все тесты пройдены")
    except SystemExit as e:
        # Тесты завершились, это нормально
        sys.exit(e.code)
    except Exception as e:
        print(f"❌ Ошибка при запуске тестов: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
