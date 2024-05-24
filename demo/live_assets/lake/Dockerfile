FROM python:3.9-slim

WORKDIR /app

RUN pip install prometheus_client flask

COPY lake_app.py lake_app.py

CMD ["python", "lake_app.py"]
