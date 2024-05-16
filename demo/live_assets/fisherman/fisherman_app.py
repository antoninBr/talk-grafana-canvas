import random
import time
from prometheus_client import start_http_server, Counter

# Initialisation du compteur Prometheus
fish_counter = Counter('fish_caught', 'Number of fishes caught by the fisherman')

def main():
    # Démarrage du serveur HTTP pour exposer les métriques Prometheus
    start_http_server(8000)
    
    while True:
        # Génération d'un nombre aléatoire de poissons pêchés entre 0 et 10
        fish_caught = random.randint(0, 5)
        # Incrémentation du compteur Prometheus
        fish_counter.inc(fish_caught)
        # Attente de 5 secondes avant de générer un nouveau nombre
        time.sleep(30)

if __name__ == "__main__":
    main()