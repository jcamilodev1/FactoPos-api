# Usa una imagen base de Python ligera
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo los archivos de requerimientos primero para aprovechar la cache de Docker
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos restantes del proyecto al directorio de trabajo
COPY . /app

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
