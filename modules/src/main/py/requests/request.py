import requests

req = requests.get('https://w3schools.com/python/demopage.htm')

print(req.text)