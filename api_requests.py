import requests
from opencage.geocoder import OpenCageGeocode
import pandas as pd
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
jsonResponse = response.json()

# posting_set = set()

#CSV columns list
company_list = []
location_list = []
title_list = []
type_list = []
company_url_list = []
description_list = []
company_logo_list = []

latitude_list = []
longitude_list = []


for i,v in enumerate(jsonResponse):
    query_string = ''
    company_name = ''
    location_name = ''
    title = ''
    type_name = ''
    description_name = ''
    company_url = ''
    company_logo = ''

    for key, value in jsonResponse[i].items():
        if key == 'title':
            title = value

        if key == 'type':
            type_name = value

        if key == 'company_url':
            company_url = value

        if key == 'company_logo':
            company_logo = value

        if key == 'description':
            description_name = value

        if key == 'location':
            location_name = value
            query_string += value

        if key == 'company':
            company_name = value
            query_string += value
            query_string += ' '

        # if (query_string == '' or query_string in posting_set):
        #     continue

        title_list.append(title)
        type_list.append(type_name)
        company_url_list.append(company_url)
        company_logo_list.append(company_logo)
        description_list.append(description_name)
        company_list.append(company_name)
        location_list.append(location_name)

        #Forward Geocoding
        key = 'fb9265b8100043e4b053b18ca019e4fe'
        geocoder = OpenCageGeocode(key)

        query = query_string

        # posting_set.add(query_string)
        results = geocoder.geocode(query)

        if results and results[0]['components']['country_code'] == 'us':
            latitude_list.append(results[0]['geometry']['lat'])
            longitude_list.append(results[0]['geometry']['lng'])

        else:
            latitude_list.append('')
            longitude_list.append('')


#Creating dataframe
dict = {'company': company_list, 'location': location_list, 'type': type_list, 'title': title_list,
'description': description_list, 'company_url': company_url_list, 'company_logo': company_logo_list,'latitude': latitude_list, 'longitude' : longitude_list}

df = pd.DataFrame(dict)
df = df.drop_duplicates(subset='company', keep='last')
df = df[df.latitude != '']

df.to_csv('data/job_search_info.csv')
