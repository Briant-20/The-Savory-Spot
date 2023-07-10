from django.views import generic
from .models import Body


class Body(generic.ListView):
    model = Body
    template_name = "index.html"
