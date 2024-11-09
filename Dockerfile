# Imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la app
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto de la aplicación
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
