#!/bin/bash
# Espera a que la base de datos esté lista
while ! nc -z db 5432; do
  echo "Esperando a que la base de datos esté disponible..."
  sleep 3
done

# Ejecutar migraciones
alembic upgrade head

# Iniciar la aplicación
exec uvicorn app.main:app --host 0.0.0.0 --port 80
