import time
import requests
from prometheus_client import start_http_server, Gauge

# Initialisation du métrique Prometheus
fireplace_gauge = Gauge('fireplace_status', 'Status of the fireplace (1 for on, 0 for off)')

def is_fireplace_on():
    try:
        print("lake-app-api call")
        # Call the lake-app-api to check if a fish can be caught
        response = requests.get('http://lake-app-api.drawing.svc.cluster.local:5000/fog')
        if response.status_code == 200:
            data = response.json()
            if data.get('is_fog'):
                print("Foggy weather!")
                return 1  # Cheminée allumée
    except requests.RequestException as e:
        print(f"Error calling lake-app-api: {e}")      
 
    return 0  # Cheminée éteinte

def main():

    # Démarrage du serveur HTTP pour exposer les métriques Prometheus
    start_http_server(8000)
    
    while True:
        # Obtention du statut actuel de la cheminée
        fireplace_status = is_fireplace_on()
        # Mise à jour du métrique Prometheus
        fireplace_gauge.set(fireplace_status)
        # Attente de 1 minute avant de vérifier à nouveau
        time.sleep(60)

if __name__ == "__main__":
    print('cabin_app starting : v3')
    main()
