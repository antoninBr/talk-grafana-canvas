# Utiliser l'image Python officielle
FROM python:3.9-slim

# Installation des dépendances
RUN pip install prometheus_client flask requests flask-cors

# Copie du code source dans le conteneur
COPY . /app
WORKDIR /app

# Exposition des ports utilisés par l'application
EXPOSE 8000 5000

# Commande pour exécuter l'application
CMD ["python", "fisherman_app.py"]