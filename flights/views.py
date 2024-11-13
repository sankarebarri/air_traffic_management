from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Flights

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from airports.models import Airport
from datetime import datetime

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


from django.utils import timezone
@csrf_exempt  # Only for testing; recommended to remove for production with proper CSRF handling
def create_flight_plan(request):
    if request.method == 'POST':
        # print("Received POST data in Django:", request.POST)
        # for key, value in request.POST.items():
        #     print(f"{key}: {value}")  # Log each key-value pair in the Django console
        call_sign = request.POST.get('callSign')
        departure_airport_code = request.POST.get('departureAirport')
        arrival_airport_code = request.POST.get('arrivalAirport')
        departure_time = request.POST.get('departureTime')
        flight_level_requested = request.POST.get('flightLevel')
        routes = request.POST.get('route')
        # weather_conditions = request.POST.get('weatherConditions', '')
        # wind_speed = request.POST.get('windSpeed', '')
        try:
            departure_airport = Airport.objects.get(icao_code=departure_airport_code)
            arrival_airport = Airport.objects.get(icao_code=arrival_airport_code)
        except Airport.DoesNotExist:
            return JsonResponse({'error': 'Airport not found'}, status=400)
        
        # Convert the time string to a datetime object
        try:
            departure_time = datetime.fromisoformat(departure_time)
            departure_time = timezone.make_aware(departure_time)
        except ValueError:
            return JsonResponse({'error': 'Invalid departure time format'}, status=400)
        print(
            call_sign, departure_airport_code,
            arrival_airport_code, departure_time,
            flight_level_requested, routes
        )
        
        flight = Flights.objects.create(
            call_sign=call_sign,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_time=departure_time,
            flight_level_requested=flight_level_requested,
            routes=routes,
            status='Scheduled',  # Default to scheduled
            regime='Commercial',  # Example default regime
            aircraft_speed=450,  # Placeholder; could be a form field
            turbulence_category='Medium',  # Placeholder
            aircraft_type='Boeing 737'  # Placeholder
        )
        return JsonResponse({'message': 'Form submitted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
