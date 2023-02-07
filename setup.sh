#!/bin/sh
cd ..

# Instalar pipenv
pip install pipenv

# Crear entorno virtual con pipenv
pipenv install

# Activar entorno virtual
pipenv shell

# Instalar dependencias para el backend de Django
pip install -r requirements.txt

# Realizar migraciones en la base de datos
cd aquaponics_django
python manage.py migrate

# Correr el servidor de Django
python manage.py runserver

# Correr el servidor de Vue
cd ../aquaponics_vue 
npm run serve 

# Esperar a que ambos procesos finalicen
#wait
