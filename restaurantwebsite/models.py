from django.db import models
from cloudinary.models import CloudinaryField


class Body(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    links = models.ManyToManyField('self', blank=True, symmetrical=False)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Button(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    information = models.TextField()
