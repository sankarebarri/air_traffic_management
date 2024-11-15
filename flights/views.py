from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Flights

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from airports.models import Airport
from datetime import datetime

from django.db.models import Q
from django.contrib import messages

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

# from django.utils import timezone
# @csrf_exempt  # For testing; recommended to remove for production with proper CSRF handling
# def create_flight_plan(request):
#     if request.method == 'POST':
#         print("Received POST data:", request.POST)
#         # Collecting data from request
#         call_sign = request.POST.get('callSign')
#         departure_airport_code = request.POST.get('departureAirport')
#         arrival_airport_code = request.POST.get('arrivalAirport')
#         departure_time = request.POST.get('departureTime')
#         flight_level_requested = request.POST.get('flightLevel')
#         routes = request.POST.get('route')

#         # Verify and retrieve Airport instances
#         try:
#             departure_airport = Airport.objects.get(icao_code=departure_airport_code)
#             arrival_airport = Airport.objects.get(icao_code=arrival_airport_code)
#         except Airport.DoesNotExist:
#             print("Airport Lookup Error:", e)
#             return JsonResponse({'error': 'One or both airports not found'}, status=400)
#             messages.error(request, "One or both airports could not be found.")
#             return redirect(request.META.get('HTTP_REFERER', '/'))
#             # return JsonResponse({'error': 'Airport not found'}, status=400)

#         # Convert departure_time to timezone-aware datetime
#         try:
#             departure_time = datetime.fromisoformat(departure_time)
#             if timezone.is_naive(departure_time):  # If naive, make it timezone-aware
#                 departure_time = timezone.make_aware(departure_time)
#         except ValueError:
#             print("Date Parsing Error:", e)
#             return JsonResponse({'error': 'Invalid departure time format'}, status=400)
#             messages.error(request, "Invalid departure time format.")
#             return redirect(request.META.get('HTTP_REFERER', '/'))
#             # return JsonResponse({'error': 'Invalid departure time format'}, status=400)
#         # print("Parsed departure time:", departure_time)
#         arrival_time = departure_time + timedelta(hours=2) 
#         # Printing to confirm collected data before creation
#         print(
#             call_sign, departure_airport_code,
#             arrival_airport_code, departure_time,
#             flight_level_requested, routes
#         )
#         print("Airports in DB:", Airport.objects.values_list('icao_code', flat=True))


#         # Try creating a flight entry
#         try:
#             flight = Flights.objects.create(
#                 call_sign=call_sign,
#                 departure_airport=departure_airport,
#                 arrival_airport=arrival_airport,
#                 departure_time=departure_time,
#                 arrival_time=arrival_time,
#                 flight_level_requested=int(flight_level_requested),  # Ensure integer conversion
#                 routes=routes,
#                 status='Scheduled',  # Default to scheduled
#                 regime='Commercial',  # Default regime
#                 aircraft_speed=450,  # Placeholder speed
#                 turbulence_category='Medium',  # Placeholder turbulence
#                 aircraft_type='Boeing 737'  # Placeholder aircraft type
#             )
#             # print("Flight created successfully:", flight)
#             messages.success(request, f"Flight plan for {call_sign} created successfully.")
#             return redirect('flight_strip', flight_id=flight.id)
#             # return JsonResponse({'message': 'Form submitted successfully'}, status=200)
#         except Exception as e:
#             # print("Error creating flight:", e)
#             messages.error(request, f'An error occured: {str(e)}')
#             # return redirect(request.META.get('HTTP_REFERER', '/'))
#             print("Error:", e)
#             print("Flight Creation Error:", e)
            
#             return JsonResponse({'error': str(e)}, status=500)
#     messages.error(request, "Invalid request method.")
#     return redirect(request.META.get('HTTP_REFERER', '/'))
#     # return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
from airports.models import Airport
from flights.models import Flights
from datetime import datetime, timedelta

def create_flight_plan(request):
    if request.method == 'POST':
        try:
            # Extract and clean data from POST
            call_sign = request.POST.get('callSign', '').strip()
            
            # Check if registration_number already exists
            registration_number = request.POST.get('registrationNumber', '').strip()
            if Flights.objects.filter(registration_number=registration_number).exists():
                messages.error(request, 'Registration number already exists.')
                return redirect(request.META.get('HTTP_REFERER', '/'))


            departure_airport_code = request.POST.get('departureAirport', '').strip()
            arrival_airport_code = request.POST.get('arrivalAirport', '').strip()
            departure_time = request.POST.get('departureTime', '').strip()
            flight_level_requested = request.POST.get('flightLevel', '').strip()
            routes = request.POST.get('route', '').strip()

            # Validate and fetch airports
            departure_airport = Airport.objects.get(icao_code__iexact=departure_airport_code)
            arrival_airport = Airport.objects.get(icao_code__iexact=arrival_airport_code)

            # Parse and validate departure time
            try:
                departure_time = datetime.fromisoformat(departure_time)
                if timezone.is_naive(departure_time):  # If naive, make it timezone-aware
                    departure_time = timezone.make_aware(departure_time)
            except ValueError:
                messages.error(request, 'Invalid departure time format.')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            # Calculate arrival time (for demonstration, assuming 2 hours flight duration)
            arrival_time = departure_time + timedelta(hours=2)

            # Debugging logs
            print(
                call_sign, departure_airport_code, departure_airport,
                arrival_airport_code, departure_time, arrival_airport,
                arrival_time, flight_level_requested, routes
            )
            print("Airports in DB:", Airport.objects.values_list('icao_code', flat=True))

            # Create the flight record
            Flights.objects.create(
                call_sign=call_sign,
                registration_number=registration_number,
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_time=departure_time,
                arrival_time=arrival_time,
                flight_level_requested=int(flight_level_requested),
                routes=routes,
                status='Scheduled',  # Default to scheduled
                regime='Commercial',  # Example default regime
                aircraft_speed=450,  # Placeholder
                turbulence_category='Medium',  # Placeholder
                aircraft_type='Boeing 737'  # Placeholder
            )

            # Success message and redirect
            messages.success(request, f"Flight plan for {call_sign} created successfully.")
            return redirect('flight_strip', flight_id=Flights.objects.latest('id').id)

        except Airport.DoesNotExist:
            messages.error(request, 'Invalid departure or arrival airport code.')
        except Exception as e:
            print(f"Error creating flight plan: {e}")
            messages.error(request, 'An error occurred while creating the flight plan.')

    # Redirect back to the referring page if something goes wrong
    return redirect(request.META.get('HTTP_REFERER', '/'))
