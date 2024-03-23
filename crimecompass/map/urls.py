from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.map, name="map"),
    path("home/", views.home, name="home")
]