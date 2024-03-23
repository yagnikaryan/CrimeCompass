from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.map, name="map"),  # Added path for map_and_directions view
    path("home/", views.home, name="home"),
    # Ensure that the 'map' view is still correctly defined if needed
]