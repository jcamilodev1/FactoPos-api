FROM python:3.9-slim-buster

# Instalar el cliente de PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copia el script wait-for-db.sh
COPY wait-for-db.sh /usr/local/bin/wait-for-db.sh
RUN chmod +x /usr/local/bin/wait-for-db.sh

# Ejecutar el script wait-for-db.sh para esperar la base de datos y luego iniciar la aplicación
ENTRYPOINT ["/usr/local/bin/wait-for-db.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
