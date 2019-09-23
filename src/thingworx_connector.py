import requests
import datetime

headers = {
    'Content-Type': "application/json",
    'appKey': "XXX",
    'Accept': "application/json",
    'x-thingworx-session': "true",
    'Cache-Control': "no-cache",
    'Host': "XXX.devportal.ptc.io",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "18",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

def send_temprerature(location, temperature):
    url = f"https://pp-1908301841xm.devportal.ptc.io/Thingworx/Things/WeatherStation{location}Thing/Services/set_temprerature"
    now = datetime.datetime.now()
    payload = "{\"value\": \"" + str(temperature) + "\"}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print('{}: temperature: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"), response.status_code))

def send_pressure(location, pressure):
    url = f"https://pp-1908301841xm.devportal.ptc.io/Thingworx/Things/WeatherStation{location}Thing/Services/set_pressure"
    now = datetime.datetime.now()
    payload = "{\"value\": \"" + str(pressure) + "\"}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print('{}: pressure: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"), response.status_code))

def send_humidity(location, humidity):
    url = f"https://pp-1908301841xm.devportal.ptc.io/Thingworx/Things/WeatherStation{location}Thing/Services/set_humidity"
    now = datetime.datetime.now()
    payload = "{\"value\": \"" + str(humidity) + "\"}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print('{}: humidity: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"), response.status_code))

def send_wind_speed(location, wind_speed):
    url = f"https://pp-1908301841xm.devportal.ptc.io/Thingworx/Things/WeatherStation{location}Thing/Services/set_wind_speed"
    now = datetime.datetime.now()
    payload = "{\"value\": \"" + str(wind_speed) + "\"}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print('{}: wind speed: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"), response.status_code))