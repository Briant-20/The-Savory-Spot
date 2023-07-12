from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuListView.as_view(), name='home'),
]
