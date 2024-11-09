from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Flights

from django.db.models import Q

class FlightListView(generic.ListView):
    model = Flights
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'

def scheduled_flights_view(request):

    context = {
        'flights': Flights.objects.filter(Q(status='Scheduled') | Q(status='Delayed') | Q(status='Cancelled'))
    }

    return render(request, 'flights/scheduled_flights.html', context)

def current_flights_view(request):

    context = {
        'flights': Flights.objects.filter(Q(status='Departed') | Q(status='Arrived'))
    }

    return render(request, 'flights/current_flights.html', context)
