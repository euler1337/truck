import requests
import json

url      = 'http://0.0.0.0:5000/api/v0.1/register'
contents =  { 'name' : 'curry-bilen', 'longitude' : '18.0765917', 'latitude' : '59.3281778'}
headers  =  {'content-type' : 'application/json'}

r = requests.post(url, json=contents)
print(r.status_code)