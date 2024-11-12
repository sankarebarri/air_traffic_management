from django.core.management.base import BaseCommand
from airports.models import Airport
from flights.models import Flights
from users.models import User

import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Populate the database with fake data for development test"

    def handle(self, *args, **kwargs):
        self.create_users()
        self.create_airports()
        self.create_flights()

    
    def create_users(self):
        usernames = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Ivy", "Jack"]
        # profile_images = [f"https://picsum.photos/seed/{username}/200" for username in usernames]

        for username in usernames:
            user = User.objects.create_user(
                username=username,
                password="123456", 
                email=f"{username}@yahoo.com",
                role=random.choice(["Controller", "Pilot"])
            )
            print(f"{username} created")

    
    def create_airports(self):
        countries = ["Mali", "Burkina", "Niger", "Senegal", "Cote d'Ivoire"]
        cities = ["Bamako", "Ougadougou","Niamey", "Dakar", "Abidjan"]

        icao_codes = set()
        iata_codes = set()
        for i in range(20):
            while True:
                icao_code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4))
                if icao_code not in icao_codes:
                    icao_codes.add(icao_code)
                    break
            while True:
                iata_code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
                if iata_code not in iata_codes:
                    iata_codes.add(icao_code)
                    break
            country = random.choice(countries)
            city = random.choice(cities)

            airport = Airport.objects.create(
                icao_code=icao_code,
                iata_code=iata_code,
                country=country,
                city=city,
                full_name=f"{city} - {iata_code} International Airport",
                abbreviated_name=f"{city}- {iata_code} Int'l",
                altitude = random.randint(1000, 4000),
                runway_length=random.randint(2500, 4000),
                runway_width=random.randint(40, 80),
                tower_frequency=f"{random.randint(100, 150)}, {random.randint(200, 300)}",
                acc_frequency=f"{random.randint(1000, 9999)}|{random.randint(1000, 9999)}",
            )
            print(f"{airport} Created")


    def create_flights(self):
        airports = list(Airport.objects.all())
        aircraft_types = ["Boeing 737", "Airbus A320", "Cessna 172", "Gulfstream G650"],

        for i in range(100):
            departure_airport = random.choice(airports)
            arrival_airport = random.choice([a for a in airports if a != departure_airport])
            departure_time = datetime.now() + timedelta(days=random.randint(0, 10))
            arrival_time = datetime.now() + timedelta(hours=random.randint(1, 12))

            flight = Flights.objects.create(
                call_sign="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6)),
                registration_number="REG"+"".join(random.choices("0123456789", k=4)),
                aircraft_type=random.choice(aircraft_types),
                aircraft_speed=random.randint(400, 600),
                turbulence_category=random.choice(['Heavy', 'Medium', 'Light']),
                routes=f"Route from {departure_airport.city} to {arrival_airport.city}",
                flight_level_requested=random.randint(280, 400),
                squawk=''.join(random.choices("0123456789", k=4)),
                # deviation_airports="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4)),
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_time=departure_time,
                arrival_time=arrival_time,
                status=random.choice(['Scheduled', 'Delayed', 'Departed', 'Arrived', 'Cancelled']),
                regime=random.choice(['Private', 'Military', 'Commercial']),
            )
            print(f"Created Flight: {flight}")


