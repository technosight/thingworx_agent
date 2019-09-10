import requests
import json

def get_data(location='Newbury,uk'):

    url = "http://api.openweathermap.org/data/2.5/weather"

    querystring = {
        "q":location,
        "units":"metric",
        "appid": "XXXX"
    }

    payload = ""
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "48c127da-3075-4ec9-b023-7536fc460306"
        }

    try:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        return json.loads(response.text)
    except:
        return None