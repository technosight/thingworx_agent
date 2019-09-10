import openweathermap
import thingworx_connector as conn
import time

if __name__ == '__main__':

    locations = [
        'Newbury',
        'London',
        'Edinburgh'
    ]

    result = {}

    while True:
        for i in locations:
            print(f'\nLocation: {i}')
            response = openweathermap.get_data(f'{i},uk')
            if response:
                temperature = response.get('main').get('temp')
                pressure = response.get('main').get('pressure')
                humidity = response.get('main').get('humidity')
                wind_speed = response.get('wind').get('speed')

                conn.send_temprerature(i, temperature)
                conn.send_pressure(i, pressure)
                conn.send_humidity(i, humidity)
                conn.send_wind_speed(i, wind_speed)
        time.sleep(5)