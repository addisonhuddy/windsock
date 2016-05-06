import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    data = requests.get('http://192.168.33.10:8181/gemfire-api/v1/windsock/2').content
    json_data = json.loads(data)
    response = make_response(json.dumps(json_data['wind']))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
