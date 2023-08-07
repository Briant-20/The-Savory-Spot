from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .models import Reservation
from .views import create


class TestReservationView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('user', 'test@gmail.com', 'password')
        self.factory = RequestFactory()

    def test_get_reservation(self):
        response = self.client.get('/reservation/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation.html')

    def test_get_edit_reservation(self):
        response = self.client.get('/edit_reservation/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_reservation.html')

    def test_create_reservation(self):
        url = 'http://127.0.0.1:8000/reservation/'
        request = self.factory.post(url, {
            'year': '2023',
            'month': '08',
            'day': '02',
            'time': '12:00',
        })
        request.user = self.user

        request.session = {}

        result1 = create(request)
        result2 = create(request)
        result3 = create(request)
        result4 = create(request)

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertTrue(result3)

        self.assertFalse(result4)

        reservation_count = Reservation.objects.filter(user=self.user).count()
        self.assertEqual(reservation_count, 3)
