from django.test import TestCase
from .models import Menu, Category, Item


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            title='Test Menu', content='Test Content')
        self.category = Category.objects.create(
            menus=self.menu, title='Test Category')
        self.item = Item.objects.create(
            categories=self.category, name='Test Item',
            description='Test Description', price=10.00)

    def test_menu_creation(self):
        self.assertEqual(str(self.menu), 'Test Menu')

    def test_category_creation(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_item_creation(self):
        self.assertEqual(str(self.item), 'Test Item')
