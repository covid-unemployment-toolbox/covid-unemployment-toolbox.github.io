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
    query_string = ''
    for key, value in jsonResponse[i].items():
        if key == 'location':
            query_string += value

        if key == 'company':
            query_string += value
            query_string += ' '

        if (query_string == ''):
            continue


        #Forward Geocoding
        key = 'e6cdbf647b42473a82025fe1c6dbf63f'
        geocoder = OpenCageGeocode(key)

        print(query_string)
        query = query_string
        results = geocoder.geocode(query)

        for i,v in enumerate(results):
            if results[i]['components']['country_code'] == 'us':
                print(u'%f;%f;%s;%s' % (results[i]['geometry']['lat'],
                                        results[i]['geometry']['lng'],
                                        results[i]['components']['country_code'],
                                        results[i]['annotations']['timezone']['name']))


        
