from django.contrib import admin
from .models import Airport

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('abbreviated_name', 'icao_code', 'city', 'country')
    search_fields = ('abbreviated_name', 'icao_code', 'iata_code')
