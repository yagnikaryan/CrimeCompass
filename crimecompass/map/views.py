from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


# Create your views here.

def index(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render())

def map(request):
    # Extracting the form data from the request's GET parameters
    start_address = request.GET.get('startAddress', '')
    end_address = request.GET.get('endAddress', '')

    # Pass the addresses to the template context
    context = {
        'start_address': start_address,
        'end_address': end_address,
    }
    return render(request, 'map.html', context)

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.map, name="map"),  # Added path for map_and_directions view
    path("home/", views.home, name="home"),
    # Ensure that the 'map' view is still correctly defined if needed
]
