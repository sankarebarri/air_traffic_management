from django.urls import path
from . import views

urlpatterns = [
    path('weather-reports/', views.weather_reports_view, name='weather_reports'),
    path('metar/create/', views.METARCreateView.as_view(), name='metar_create'),
    path('taf/create/', views.TAFCreateView.as_view(), name='taf_create'),
    path('sigmet/create/', views.SIGMETCreateView.as_view(), name='sigmet_create'),
]