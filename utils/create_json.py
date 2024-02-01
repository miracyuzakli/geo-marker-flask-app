from geopy.geocoders import Nominatim
import pandas as pd


def get_city_coordinates(city_name):
    # Geocoder servisini başlat
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Şehrin konumunu bul
    location = geolocator.geocode(city_name)

    # Enlem ve boylamı döndür
    return [location.latitude, location.longitude]


