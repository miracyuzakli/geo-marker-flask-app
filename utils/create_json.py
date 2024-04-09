# from geopy.geocoders import Nominatim
# import pandas as pd


# def get_city_coordinates(city_name):
#     # Geocoder servisini başlat
#     geolocator = Nominatim(user_agent="geoapiExercises")

#     # Şehrin konumunu bul
#     location = geolocator.geocode(city_name)

#     # Enlem ve boylamı döndür
#     return [location.latitude, location.longitude]


# print(get_city_coordinates("Alisa Craig"))


from geopy.geocoders import Nominatim
import pandas as pd

def get_city_coordinates(city_name, country='ca'):
    # Geocoder servisini başlat
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Şehrin konumunu bul, sadece belirtilen ülkede ara
    location = geolocator.geocode(f"{city_name}, {country}")

    # Eğer konum bulunamazsa None döndür
    if location is None:
        return None

    # Enlem, boylam ve ülkeyi döndür
    return [location.latitude, location.longitude, location.address]

# Örnek kullanım
# print(get_city_coordinates("Alisa Craig"))

data = pd.read_excel('utils/City list for Boran.xlsx')

data_dict = dict()
i = 0
for city in data["cities"]:
    i += 1
    print(i)
    try:
        data_dict[city] = get_city_coordinates(city_name=city)
    except:
        print(city)

print(data_dict)