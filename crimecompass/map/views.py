from django.shortcuts import render, redirect
from urllib.parse import quote
from django.http import HttpResponse
from django.template import loader
from .forms import RouteForm
import requests



# Create your views here.

def index(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render())


def map_and_directions(request):
    # Your OpenRouteService API Key
    api_key = '5b3ce3597851110001cf624847bbb5db0d234327a7a7a31de91d3134'

    # Coordinates (longitude, latitude) for the start and end points
    start_coord = (8.681495, 49.41461)  # Example coordinates
    end_coord = (8.687872, 49.420318)  # Example coordinates
    # start_coord = request.session.get('start_coord')
    # end_coord = request.session.get('end_coord')

    # OpenRouteService Directions API endpoint
    url = f"https://api.openrouteservice.org/v2/directions/driving-car"

    # Headers and parameters for the API call
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    params = {
        'start': f'{start_coord[0]},{start_coord[1]}',
        'end': f'{end_coord[0]},{end_coord[1]}'
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the geometry (route) from the response
        route = response.json()['features'][0]['geometry']
        # Pass the route to the template
        context = {'route': route}
    else:
        context = {'error': 'Could not fetch directions.'}

    return render(request, 'your_template.html', context)

def map(request):
    starting_location = request.session.get('starting_location', 'Not specified')
    destination = request.session.get('destination', 'Not specified')
    start_coords = request.session.get('start_coords')
    dest_coords = request.session.get('dest_coords')

    start_lat = start_coords['lat'] if start_coords else None
    start_lng = start_coords['lng'] if start_coords else None
    dest_lat = dest_coords['lat'] if dest_coords else None
    dest_lng = dest_coords['lng'] if dest_coords else None

    context = {
        'starting_location': starting_location,
        'destination': destination,
        'start_lat': start_lat,
        'start_lng': start_lng,
        'dest_lat': dest_lat,
        'dest_lng': dest_lng,
    }
    return render(request, 'map.html', context)



def home(request):
    form = RouteForm()
    return render(request, 'home.html', {'form': form})
 # Make sure you have this library

from urllib.parse import quote
import requests

def submit_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            starting_location = form.cleaned_data['starting_location']
            destination = form.cleaned_data['destination']
            encoded_starting_location = quote(starting_location)
            encoded_destination = quote(destination)
            
            geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
            api_key = "AIzaSyBvvPh3svO6R-gM3GOblmmZXrKc56YoNnw" 

            start_response = requests.get(f"{geocode_url}?address={encoded_starting_location}&key={api_key}")
            start_data = start_response.json()
            start_coords = start_data['results'][0]['geometry']['location'] if start_data['results'] else None

            dest_response = requests.get(f"{geocode_url}?address={encoded_destination}&key={api_key}")
            dest_data = dest_response.json()
            dest_coords = dest_data['results'][0]['geometry']['location'] if dest_data['results'] else None

            if start_coords and dest_coords:
                request.session['starting_location'] = starting_location
                request.session['destination'] = destination
                request.session['start_coords'] = start_coords
                request.session['dest_coords'] = dest_coords

            return redirect('map')
    else:
        form = RouteForm()
    return render(request, 'home.html', {'form': form})
