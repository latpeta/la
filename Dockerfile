# Usa una imagen base de Python (puedes ajustar la versión si lo necesitas)
FROM python:3.10.12

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias y lo instala
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Expone el puerto en el que correrá la aplicación (Flask por defecto usa 5000)
EXPOSE 5500

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
