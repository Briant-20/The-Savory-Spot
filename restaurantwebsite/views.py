from django.views import generic
from .models import Menu, Button


class Menu(generic.ListView):
    model = Menu
    template_name = "index.html"


class Button(generic.ListView):
    model = Button