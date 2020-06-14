import requests
from opencage.geocoder import OpenCageGeocode
import flask
from flask import request
from flask import jsonify
import urlparse
# from pprint import pprint
app = flask.Flask(__name__)
# @app.route('/',methods=['GET', 'POST', 'PUT'])
# def pass_val():
#     # search_address = request.args.get('search_address')
#     # print('search_address', search_address)
#     print("hello")
#     return jsonify({'reply':'success'})

# pass_val()
print(request.GET.get('address'))
url = 'https://post-covid-job-tracker.github.io/'

par = urlparse.parse_qs(urlparse.urlparse(url).query)

print par['address'][0], par['p'][0]

# @app.route('/', methods = ['POST'])
# def get_post_javascript_data():
#     address = request.args.get('address')
#     # password = request.args.get('password')
#     print("hello")
#     return address

# jsdata = get_post_javascript_data()
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
        key = 'fb9265b8100043e4b053b18ca019e4fe'
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



# @app.route('/py', methods=['GET', 'POST'])
# def server():
#     if request.method == 'POST':
#         # Then get the data from the form
#         tag = request.form['tag']

#         # Get the username/password associated with this tag
#         user, password = tag_lookup(tag)

#         # Generate just a boring response
#         return 'The credentials for %s are %s and %s' % (tag, user, password) 
#         # Or you could have a custom template for displaying the info
#         # return render_template('asset_information.html',
#         #                        username=user, 
#         #                        password=password)

#     # Otherwise this was a normal GET request
#     else:   
#         return render_template('index.html')

