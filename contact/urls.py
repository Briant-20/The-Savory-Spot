from . import views
from django.urls import path

urlpatterns = [
    path('contact', views.ContactView.as_view(), name='contact'),
]
