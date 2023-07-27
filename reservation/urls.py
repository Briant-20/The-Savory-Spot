from . import views
from django.urls import path

urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('edit_reservation/', views.EditReservationView.as_view(), name='edit_reservation'),
]
