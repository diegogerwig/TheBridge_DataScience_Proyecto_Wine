# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Hace que el puerto 80 esté disponible para el mundo fuera de este contenedor
EXPOSE 80

# Define la variable de entorno
ENV NAME WineClassifier

# Ejecuta la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "fastapi_wine_api:app", "--host", "0.0.0.0", "--port", "80"]
