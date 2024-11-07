from django.contrib import admin
from .models import Flights

@admin.register(Flights)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('call_sign', 'departure_airport', 'arrival_airport', 'status', 'departure_time', 'arrival_time')
    search_fields = ('call_sign', 'registration_number')
    list_filter = ('status', 'turbulence_category', 'regime')