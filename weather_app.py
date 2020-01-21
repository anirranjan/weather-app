import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/city')
def search_city():
    API_KEY = 'eb4574ca5b64b56ed3271004097be1b1' #initalized key
    city = request.args.get('q') #city name passed as argument

    # call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

    # error like unknown city name, invalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    #get current temperature and convert it into Fahrenheit
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_fahrenheit = round(current_temperature * 9/5 - 459.67, 2)
        return f'Current temperature of {city.title()} is {current_temperature_fahrenheit} &#8457;'
    else :
        return f'Error getting temperature for {city.title()}'         


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'


if __name__ == '__main__':
    app.run(debug=True)