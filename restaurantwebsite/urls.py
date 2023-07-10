from . import views
from django.urls import path

urlpatterns = [
    path('', views.Body.as_view(), name='home'),
]
