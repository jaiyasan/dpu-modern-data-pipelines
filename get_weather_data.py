import requests


API_KEY = "8eb8a480f078a5c64790722cd947a5a8"
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}
url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=payload)
print(response.url)

data = response.json()
print(data)