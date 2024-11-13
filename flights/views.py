from django.shortcuts import render, get_object_or_404
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


def flight_strip(request, flight_id):

    
    context = {
        'flight': get_object_or_404(Flights, id=flight_id)
    }

    return render(request, 'flights/flight_strip.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for testing; recommended to remove for production with proper CSRF handling
def create_flight_plan(request):
    if request.method == 'POST':
        print("Received POST data in Django:", request.POST)
        # for key, value in request.POST.items():
        #     print(f"{key}: {value}")  # Log each key-value pair in the Django console
        return JsonResponse({'message': 'Form submitted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
