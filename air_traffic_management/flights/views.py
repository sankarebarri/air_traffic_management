from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Flights

class FlightListView(generic.ListView):
    model = Flights
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'
