from django.test import TestCase, override_settings
from contact.forms import ContactForm
from unittest.mock import patch


@override_settings(email_sender='test@example.com')
class ContactViewTest(TestCase):

    def test_get_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    @patch('smtplib.SMTP_SSL')
    def test_email_sent(self, mock_smtp):
        form_data = {
            'name': 'John Doe',
            'message': 'Hello, this is a test message.',
        }

        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post('/contact/', form_data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(mock_smtp.return_value.__enter__.return_value.sendmail.called)

        self.assertTrue(self.client.session.get('sent', False))