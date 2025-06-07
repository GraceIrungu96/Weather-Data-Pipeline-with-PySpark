import requests, json, os
from datetime import datetime

API_KEY = "cfed4f4ce780e110927920e1f259fc55"
CITY = "nairobi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q>
response = requests.get(URL)
data= response.json()

filename= f"weather.json"

os.makedirs(".", exist_ok="True")

with open(filename, "w") as f:
    json.dump(data,f )
