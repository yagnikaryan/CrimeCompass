from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.map, name="map"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("submit_route/", views.submit_route, name="submit_route"),
]