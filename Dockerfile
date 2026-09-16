# Imagen base con Python 3.11
FROM python:3.14-slim
# Establecer directorio de trabajo
WORKDIR /app
# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copiar código del proyecto
COPY . .
# Comando para ejecutar Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
