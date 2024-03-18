from datetime import datetime
from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    """Convert a timestamp to a datetime object and format it."""
    return datetime.fromtimestamp(value).strftime(format)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp',methods = ['POST'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q' : request.form.get('city'),
        'units' : request.form.get('units'),
        'appid' : 'b32d3fae6e7d25efd9320fd3b79569ae',
    }
    
    response = requests.get(url,params= param)
    data = response.json()
    return render_template('weather.html', weather_data=data)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5002)
    