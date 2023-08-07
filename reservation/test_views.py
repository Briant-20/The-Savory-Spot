from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .models import Reservation
from .views import create, delete


class TestReservationView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('user', None, 'password')
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

        reservation1 = create(request)
        reservation2 = create(request)
        reservation3 = create(request)
        reservation4 = create(request)

        self.assertTrue(reservation1)
        self.assertTrue(reservation2)
        self.assertTrue(reservation3)

        self.assertFalse(reservation4)

        reservation_count = Reservation.objects.filter(user=self.user).count()
        self.assertEqual(reservation_count, 3)

    def test_delete_reservation(self):
        url = 'http://127.0.0.1:8000/reservation/'
        request = self.factory.post(url, {
            'year': '2023',
            'month': '08',
            'day': '02',
            'time': '12:00',
        })
        request.user = self.user

        request.session = {}

        reservation = create(request)
        self.assertTrue(reservation)
        reservation_id = reservation.id
        delete(request, reservation_id, None)

        reservation_count = Reservation.objects.filter(user=self.user).count()
        self.assertEqual(reservation_count, 0)
