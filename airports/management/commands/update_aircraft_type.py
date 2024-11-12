from django.core.management.base import BaseCommand

import random
from flights.models import Flights

# def correct_aircraft_types():
#     # Define the correct aircraft types list
#     aircraft_types = ["Boeing 737", "Airbus A320", "Cessna 172", "Gulfstream G650"]

#     # Query all flights and update each one
#     flights = Flights.objects.all()
#     for flight in flights:
#         # Assign a single aircraft type randomly to each flight
#         flight.aircraft_type = random.choice(aircraft_types)
#         flight.save()
#         print(f"Updated Flight {flight.call_sign}: Aircraft Type set to {flight.aircraft_type}")

# # Run the function
# correct_aircraft_types()

class Command(BaseCommand):
    help = 'Correct aircraft_type field in Flights model with single values from aircraft_types list'

    def handle(self, *args, **kwargs):
        # Define the correct aircraft types list
        aircraft_types = ["Boeing 737", "Airbus A320", "Cessna 172", "Gulfstream G650"]

        # Query all flights and update each one
        flights = Flights.objects.all()
        for flight in flights:
            # Assign a single aircraft type randomly to each flight
            flight.aircraft_type = random.choice(aircraft_types)
            flight.save()
            self.stdout.write(self.style.SUCCESS(f"Updated Flight {flight.call_sign}: Aircraft Type set to {flight.aircraft_type}"))