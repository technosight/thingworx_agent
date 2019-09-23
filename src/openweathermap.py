import requests
import json

def get_data(location='Newbury,uk'):

    url = "http://api.openweathermap.org/data/2.5/weather"

    querystring = {
        "q":location,
        "units":"metric",
        "appid": "XXX"
    }

    payload = ""
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }

    try:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        return json.loads(response.text)
    except:
        return None