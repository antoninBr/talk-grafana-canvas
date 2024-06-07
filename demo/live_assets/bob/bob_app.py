import time
import random
from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_client import start_http_server, Counter, generate_latest

# Initialisation du compteur Prometheus
drawings_counter = Counter('drawings', 'Number of drawings made by bob')

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
    global drawings_counter
    drawings_counter._value.set(0)  # Réinitialisation du compteur à zéro
    response = jsonify(message="Counter reset to zero")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response)
    return response

def increment_drawings_counter():
    while True:
        print("Increment drawing counter")
        drawings_counter.inc(1)
        time.sleep(random.uniform(30, 90))

if __name__ == "__main__":
    print('bob_app starting : v1')
    # Démarrage du serveur HTTP pour les métriques Prometheus
    start_http_server(8000)
    
    # Démarrage de l'incrémentation du compteur dans un thread séparé
    import threading
    threading.Thread(target=increment_drawings_counter).start()
    
    # Démarrage de l'application Flask
    app.run(host='0.0.0.0', port=5000)
