# Imagen base
FROM python:3.10.11

# Definir variable de entorno.
ENV FLASK_ENV=development

# Directorio de trabajo.
WORKDIR /app

# Copiar archivos necesarios.
COPY . /app

# Instalar dependencias.
RUN pip install -r requirements.txt

# Exponer puerto 2057.
EXPOSE 2057

# Comando para correr la aplicación.
CMD ["flask", "run", "--host=0.0.0.0", "--port=2057", "--reload"]
