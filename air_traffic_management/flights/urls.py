from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.FlightListView.as_view(), name='flight_list'),
]