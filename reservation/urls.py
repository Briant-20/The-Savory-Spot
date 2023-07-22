from . import views
from django.urls import path

urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
]
