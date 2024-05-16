# Utiliser l'image Python officielle
FROM python:3.9-slim

# Installation des dépendances
RUN pip install prometheus_client

# Copie du code source dans le conteneur
COPY . /app
WORKDIR /app

# Exposition du port 8000 utilisé par l'application
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "fisherman_app.py"]