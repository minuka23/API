import requests

API = 'https://api.@Minukakevin.software/logo?name='

req = requests.post(API+input('Name : ').replace(' ','%20'))

print(req.history[1].url)
