from django.urls import path
from . import views

urlpatterns = [
    path('weather-reports/', views.weather_reports_view, name='weather_reports'),
]
