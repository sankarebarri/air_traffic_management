from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.FlightListView.as_view(), name='flight_list'),
    path('scheduled-flights/', views.scheduled_flights_view, name='scheduled_flights'),
    path('current-flights/', views.current_flights_view, name='current_flights'),
    path('flight-strip/<int:flight_id>', views.flight_strip, name='flight_strip'),
    # path('flight-strip/print/<int:flight_id>/', views.flight_strip_print_view, name='flight_strip_print'),
]
