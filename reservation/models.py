from django.db import models


class Year(models.Model):
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.year


class Month(models.Model):
    years = models.ForeignKey(Year, on_delete=models.CASCADE)
    month = models.CharField(max_length=100)

    def __str__(self):
        return self.month


class Day(models.Model):
    months = models.ForeignKey(Month, on_delete=models.CASCADE)
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.day


class Time(models.Model):
    days = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.time


class Table(models.Model):
    times = models.ForeignKey(Time, on_delete=models.CASCADE)
    table = models.CharField(max_length=100)

    def __str__(self):
        return self.table


class Reservation(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} - {self.month} - {self.day} - {self.time} - {self.table}"