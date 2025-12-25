from django.test import TestCase

class BasicTests(TestCase):
    def test_admin_page(self):
        response = self.client.get('/admin/')
        self.assertIn(response.status_code, [200, 302])
