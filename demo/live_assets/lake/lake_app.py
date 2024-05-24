from flask import Flask, jsonify
from prometheus_client import start_http_server, Gauge
import random
import threading
import time

app = Flask(__name__)

# Prometheus metric
TEMPERATURE = Gauge('lake_temperature_celsius', 'Current temperature of the lake')

# Initial temperature
temperature = 18

def update_temperature():
    global temperature
    while True:
        print("temperature update")
        # Randomly vary the temperature between 12 and 24 degrees
        temperature += random.uniform(-0.5, 0.5)
        temperature = max(12, min(24, temperature))
        TEMPERATURE.set(temperature)
        print(temperature)
        time.sleep(10)

@app.route('/catch', methods=['GET'])
def catch():
    print('catch api called')
    response = jsonify(catch_possible=15 <= temperature <= 20)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")

    print(response)
    return response

@app.route('/fog', methods=['GET'])
def fog():
    print('fog api called')
    response = jsonify(is_fog=12 <= temperature <= 17)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")

    print(response)
    return response

if __name__ == '__main__':
    print('lake_app starting: v3')
    # Start Prometheus metrics server
    start_http_server(8000)
    # Start the temperature update thread
    threading.Thread(target=update_temperature, daemon=True).start()
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)
