from django.db import models
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    links = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.title


class Button(models.Model):
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    information = models.TextField()
