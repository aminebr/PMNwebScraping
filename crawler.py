import datetime
import json
import csv
import urllib.request

def url_builder(city_id,city_name,country):
    user_api = '4e0f8959dab541379b863bd8868196a6'  # Obtain yours form: http://openweathermap.org/ https://openweathermap.org/current
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    if(city_name!=""):
        api = 'http://api.openweathermap.org/data/2.5/weather?q=' # "http://api.openweathermap.org/data/2.5/weather?q=Tunis,TN
        full_api_url = api + str(city_name) +','+ str(country)+ '&mode=json&units=' + unit + '&APPID=' + user_api
    else:
        api = 'http://api.openweathermap.org/data/2.5/weather?id='# Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz
        full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url



def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)#convertir une chaine comme dictionnaire
    #print(type(output))
    #print(type(raw_api_dict))
    url.close()#fermer la connexion au serveur api
    return raw_api_dict