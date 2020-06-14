import requests
from opencage.geocoder import OpenCageGeocode
from pprint import pprint



response = requests.get('https://jobs.github.com/positions.json?&full_time=true&location=gurnee')
response.raise_for_status()
# access JSOn content
jsonResponse = response.json()
print("Entire JSON response")
print(jsonResponse)


key = 'e6cdbf647b42473a82025fe1c6dbf63f'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(44.8303087, -0.5761911)
pprint(results)
# [{'components': {'city': 'Bordeaux',
#                  'country': 'France',
#                  'country_code': 'fr',
#                  'county': 'Bordeaux',
#                  'house_number': '11',
#                  'political_union': 'European Union',
#                  'postcode': '33800',
#                  'road': 'Rue Sauteyron',
#                  'state': 'New Aquitaine',
#                  'suburb': 'Bordeaux Sud'},
#   'formatted': '11 Rue Sauteyron, 33800 Bordeaux, France',
#   'geometry': {'lat': 44.8303087, 'lng': -0.5761911}}]