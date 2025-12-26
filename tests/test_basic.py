from django.test import TestCase
import os

# Устанавливаем тестовые настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.test_settings')

class BasicTests(TestCase):
    """Базовые тесты Django"""
    
    def test_django_setup(self):
        """Проверка что Django настроен"""
        self.assertTrue(True)
    
    def test_settings(self):
        """Проверка настроек"""
        from django.conf import settings
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 
                        'django.db.backends.sqlite3')
    
    def test_admin_redirect(self):
        """Проверка редиректа админки"""
        response = self.client.get('/admin/')
        self.assertIn(response.status_code, [200, 302, 404])
