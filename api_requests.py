import requests
from opencage.geocoder import OpenCageGeocode
import pandas as pd
# from pprint import pprint
app = flask.Flask(__name__)
# @app.route('/',methods=['GET', 'POST', 'PUT'])
# def pass_val():
#     # search_address = request.args.get('search_address')
#     # print('search_address', search_address)
#     print("hello")
#     return jsonify({'reply':'success'})

# for i in range(0, 5):
# api-endpoint
URL = 'https://jobs.github.com/positions.json'

# # location given here
# location = 'new york' #enter user inputted city
# full_time = 'true'
# description = 'engineer'

# defining a params dict for the parameters to be sent to the API
PARAMS = {'page':4}

# sending get request and saving the response as response object
response = requests.get(url = URL, params = PARAMS)

# extracting data in json format
jsonResponse = response.json()
print(jsonResponse)
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
        key = '05da6b4ff4e84421b38eabbbf0a9680a'
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
dict = {'Company': company_list, 'Location': location_list, 'Type': type_list, 'Title': title_list,
'Description': description_list, 'Company_url': company_url_list, 'Company_logo': company_logo_list,'Latitude': latitude_list, 'Longitude' : longitude_list}

df = pd.DataFrame(dict)
# df = df.drop_duplicates(subset='Company', keep='last')
df = df[df.Latitude != '']

df.to_csv('data/job_search_info3.csv')
