from django.shortcuts import render

def map_view(request):
    return render(request, 'map_visualisation/map.html')
