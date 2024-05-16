import time
from prometheus_client import start_http_server, Gauge

# Initialisation du métrique Prometheus
fireplace_gauge = Gauge('fireplace_status', 'Status of the fireplace (1 for on, 0 for off)')

def is_fireplace_on():
    # Récupère l'heure actuelle
    current_hour = time.localtime().tm_hour
    # Vérifie si l'heure est entre 18h et 22h
    if 18 <= current_hour < 22:
        return 1  # Cheminée allumée
    else:
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
    main()
