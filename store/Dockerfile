# Etapa de compilación (builder)
FROM python:3.9-slim-buster AS builder
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python -m compileall .

# Etapa de producción (final)
FROM python:3.9-slim-buster
WORKDIR /app

# Copiar solo los archivos compilados desde la etapa de compilación
COPY --from=builder /app/ /app/

ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema (si es necesario)
RUN apt-get update && apt-get install -y \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Descargar e instalar wait-for-it
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /app/wait-for-it.sh && \
    chmod +x /app/wait-for-it.sh

# Exponer el puerto
EXPOSE 80

# Comando para iniciar la aplicación
CMD ["/app/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]