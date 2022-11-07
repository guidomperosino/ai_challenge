import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    
    @classmethod
    def is_hot_in_pehuajo(cls):
        temperature = temperature_on_location(f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}")
        if temperature > 28:
            return True
        else:
            return False

def temperature_on_location(url):
    try:
        payload = {'units': 'metric'}
        response = requests.get(url, params = payload)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            return temp
    except:
        return 0