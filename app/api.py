from flask import render_template, request
from app import app
from app.crawler import url_builder, data_fetch
from app.db import insert_data
import json



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        city = request.form.get('city')
        country = request.form.get('country')


        full_api_url = url_builder(city, "", "")

        raw_api_dict = data_fetch(full_api_url)


        temperature = str(raw_api_dict['main']['temp'])
        weather = raw_api_dict['weather'][0]['description']


        insert_data(country,city,temperature,weather)


        return render_template('index.html', weather_data=raw_api_dict)

    return render_template('index.html')



@app.route('/get_countries')
def get_countries():
    # Load countries from the city.list.json file
    countries = set()
    with open('city.list.json', 'r', encoding='utf-8') as json_file:
        cities = json.load(json_file)
        for city in cities:
            countries.add(city['country'])
    return json.dumps(list(countries))

@app.route('/get_cities')
def get_cities():
    selected_country = request.args.get('country')
    cities = []
    with open('city.list.json', 'r', encoding='utf-8') as json_file:
        all_cities = json.load(json_file)
        for city in all_cities:
            if city['country'] == selected_country:
                cities.append({'id': city['id'], 'name': city['name']})
    return json.dumps(cities)