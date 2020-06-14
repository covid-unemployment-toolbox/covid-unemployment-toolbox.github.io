import requests


response = requests.get('https://jobs.github.com/positions.json?&full_time=true&location=gurnee')
response.raise_for_status()
# access JSOn content
jsonResponse = response.json()
print("Entire JSON response")
print(jsonResponse)
