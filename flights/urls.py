from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.FlightListView.as_view(), name='flight_list'),
    path('scheduled-flights/', views.scheduled_flights_view, name='scheduled_flights'),
    path('current-flights/', views.current_flights_view, name='current_flights'),
    path('flight-strip/<int:flight_id>', views.flight_strip, name='flight_strip'),

    path('airports/', views.AirportListView.as_view(), name='airport_list'),
    path('airports/<int:pk>/', views.AirportDetailView.as_view(), name='airport_detail'),
    
    path('create-flight-plan/', views.create_flight_plan, name='create_flight_plan'),
]
