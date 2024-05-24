import random
import time
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_client import start_http_server, Counter, generate_latest

# Initialisation du compteur Prometheus
fish_counter = Counter('fish_caught', 'Number of fishes caught by the fisherman')

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)

# Endpoint pour les métriques Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest()

# Endpoint pour réinitialiser le compteur
@app.route('/reset', methods=['POST'])
def reset_counter():
    print('reset api called')
    global fish_counter
    fish_counter._value.set(0)  # Réinitialisation du compteur à zéro
    response = jsonify(message="Counter reset to zero")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response)
    return response

def increment_fish_counter():
    while True:
        try:
            print("lake-app-api call")
            # Call the lake-app-api to check if a fish can be caught
            response = requests.get('http://lake-app-api.drawing.svc.cluster.local:5000/catch')
            if response.status_code == 200:
                data = response.json()
                if data.get('catch_possible'):
                    print("It's a catch !")
                    fish_counter.inc(1)
        except requests.RequestException as e:
            print(f"Error calling lake-app-api: {e}")        
        # Attente de 30 secondes avant de re-pêcher
        time.sleep(30)

if __name__ == "__main__":
    print('fisherman_app starting : v4')
    # Démarrage du serveur HTTP pour les métriques Prometheus
    start_http_server(8000)
    
    # Démarrage de l'incrémentation du compteur dans un thread séparé
    import threading
    threading.Thread(target=increment_fish_counter).start()
    
    # Démarrage de l'application Flask
    app.run(host='0.0.0.0', port=5000)
