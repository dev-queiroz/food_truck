from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/food-trucks', methods=['GET'])
def get_food_trucks():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    url = 'https://data.sfgov.org/resource/rqzj-sfat.json'
    
    params = {
        '$where': f'within_circle(location, {latitude}, {longitude}, 1000)'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
