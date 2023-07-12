from django.views import generic
from .models import Menu


class Menu(generic.ListView):
    model = Menu
    template_name = "index.html"
