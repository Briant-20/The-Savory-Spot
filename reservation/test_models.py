from django.test import TestCase
from .models import Year, Month, Day, Time, Table, Reservation
from django.contrib.auth.models import User


class ReservationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.year = Year.objects.create(year='2023')
        self.month = Month.objects.create(years=self.year, month='5')
        self.day = Day.objects.create(months=self.month, day='25th')
        self.time = Time.objects.create(days=self.day, time='16:00')
        self.table = Table.objects.create(times=self.time, table='1')
        self.reservation = Reservation.objects.create(
            user=self.user,
            year=self.year,
            month=self.month,
            day=self.day,
            time=self.time,
            table=self.table
        )

    def test_reservation_str_representation(self):
        string = f"DATE: {self.day} - {self.month} - {self.year} - TIME: {self.time} - TABLE: {self.table} - USER: {self.user}"
        self.assertEqual(str(self.reservation), string)
