import random
import time
from flask import Flask, jsonify
from prometheus_client import start_http_server, Counter, generate_latest

# Initialisation du compteur Prometheus
fish_counter = Counter('fish_caught', 'Number of fishes caught by the fisherman')

# Initialisation de l'application Flask
app = Flask(__name__)

# Endpoint pour les métriques Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest()

# Endpoint pour réinitialiser le compteur
@app.route('/reset', methods=['POST'])
def reset_counter():
    global fish_counter
    fish_counter._value.set(0)  # Réinitialisation du compteur à zéro
    response = jsonify(message="Counter reset to zero")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def increment_fish_counter():
    while True:
        # Génération d'un nombre aléatoire de poissons pêchés entre 0 et 10
        fish_caught = random.randint(0, 5)
        # Incrémentation du compteur Prometheus
        fish_counter.inc(fish_caught)
        # Attente de 5 secondes avant de générer un nouveau nombre
        time.sleep(30)

if __name__ == "__main__":
    # Démarrage du serveur HTTP pour les métriques Prometheus
    start_http_server(8000)
    
    # Démarrage de l'incrémentation du compteur dans un thread séparé
    import threading
    threading.Thread(target=increment_fish_counter).start()
    
    # Démarrage de l'application Flask
    app.run(host='0.0.0.0', port=5000)
