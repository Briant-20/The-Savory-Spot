from django.db import models


class Year(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Month(models.Model):
    years = models.ForeignKey(Year, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Day(models.Model):
    months = models.ForeignKey(Month, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Time(models.Model):
    days = models.ForeignKey(Day, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Table(models.Model):
    times = models.ForeignKey(Time, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
