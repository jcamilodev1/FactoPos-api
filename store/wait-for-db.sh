#!/bin/bash

# Esperar a que la base de datos esté disponible
echo "Waiting for PostgreSQL to be available..."
until pg_isready -h db -p 5432 -U factouser; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - executing command"

# Ejecutar las migraciones de Alembic
alembic upgrade head

# Ejecutar el comando proporcionado al contenedor (por defecto, iniciar la aplicación)
exec "$@"
