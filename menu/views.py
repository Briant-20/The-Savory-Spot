from django.views import generic
from .models import Menu


class MenuListView(generic.ListView):
    model = Menu
    template_name = "index.html"
    context_object_name = "menu_list"
