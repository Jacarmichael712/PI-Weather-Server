import http.client
import json
import config

baseURL = "api.openweathermap.org"

def getGeocoding(city):
    # establish connection with API host
    conn = http.client.HTTPSConnection(baseURL)
    payload = ''
    headers = {
    'api-key': config.api_key
    }

    conn.request("GET", ("//geo/1.0/direct?q={}&appid={}".format(city, config.api_key)), payload, headers)
    res = conn.getresponse() # get response from server
    data = res.read().decode("utf-8") # read and decode response
    json_data = json.loads(data) # format data as json

    # return lat, lon values for city
    return json_data[0]['lat'], json_data[0]['lon'], json_data[0]['state'], json_data[0]['country']

def getWeatherInfo(city, units):
    # establish connection with API host
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    payload = ''
    headers = {}

    # get lat and lon values by calling geocode API on city name
    lat, lon, state, country = getGeocoding(city)
    conn.request("GET", ("//data/2.5/weather?lat={}&lon={}&units={}&appid={}".format(lat, lon, units, config.api_key)), payload, headers)
    
    res = conn.getresponse() # get response from server
    data = res.read().decode("utf-8") # read and decode response
    json_data = json.loads(data) # format data as json

    if(units == 'imperial'):
        print("Current temperature is {} degrees fahrenheit in {}, {}, {}".format(json_data['main']['temp'], city, state, country))
    elif(units == 'metric'):
        print("Current temperature is {} degrees celsius in {}, {}, {}".format(json_data['main']['temp'], city, state, country))