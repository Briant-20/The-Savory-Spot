from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):

    def test_valid_contact_form(self):
        form_data = {
            'name': 'Test',
            'message': 'Test message',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        form_data = {
            'name': '',
            'message': 'Test message',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_empty_contact_form(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
