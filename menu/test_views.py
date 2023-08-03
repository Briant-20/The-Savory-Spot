from django.test import TestCase


class MenuViewTest(TestCase):

    def test_get_contact(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
