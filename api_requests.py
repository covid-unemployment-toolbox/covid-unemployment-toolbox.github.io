import requests
from opencage.geocoder import OpenCageGeocode
# from pprint import pprint

# api-endpoint
URL = 'https://jobs.github.com/positions.json'

# # location given here
location = 'new york' #enter user inputted city
full_time = 'true'
description = 'engineer'

# defining a params dict for the parameters to be sent to the API
PARAMS = {'location':location, 'full_time': full_time, 'decription':description}

# sending get request and saving the response as response object
response = requests.get(url = URL, params = PARAMS)

# extracting data in json format
# data = r.json()

# response = requests.get('https://jobs.github.com/positions.json?&full_time=full_time&location=new+york&description=')
# response.raise_for_status()
# access JSOn content
jsonResponse = response.json()
for i,v in enumerate(jsonResponse):
    for key, value in jsonResponse[i].items():
        if key == 'location':
            print(key, ":", value)
        if key == 'company':
            print(key, ":", value)
        if key == 'title':
            print(key, ":", value)


#Forward Geocoding
key = 'e6cdbf647b42473a82025fe1c6dbf63f'
geocoder = OpenCageGeocode(key)

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade