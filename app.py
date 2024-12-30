from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = "767b16ea2ceb9cdb9f0b8290e615ae0c"  # Replace with your API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={"767b16ea2ceb9cdb9f0b8290e615ae0c"}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather_data = {'error': 'City not found'}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)