from django.shortcuts import render, redirect

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
    # Retrieve the data from the session
    starting_location = request.session.get('starting_location', 'Not specified')
    destination = request.session.get('destination', 'Not specified')

    # Pass the locations to the map template
    context = {
        'starting_location': starting_location,
        'destination': destination
    }
    return render(request, 'map.html', context)


def home(request):
    form = RouteForm()
    return render(request, 'home.html', {'form': form})



def submit_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            # Save the form data to the session
            request.session['starting_location'] = form.cleaned_data['starting_location']
            request.session['destination'] = form.cleaned_data['destination']

            # Redirect to the map view
            return redirect('map')
    else:
        form = RouteForm()
    return render(request, 'home.html', {'form': form})