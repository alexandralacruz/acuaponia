#!/bin/sh
#cd ..
npx browserslist@latest --update-db

# Instalar pipenv
echo "instalando el ambiente virtual"


# Crear entorno virtual con pipenv
#pipenv install

#apt install python3-pip python3-setuptools python3.8-venv
#sudo apt-get install python3-pip
python3 -m venv acuaponia-env --without-pip --system-site-packages
source acuaponia-env/bin/activate


# Activar entorno virtual
#pipenv shell

# Realizar migraciones en la base de datos
cd aquaponics_django
python manage.py migrate

# Correr el servidor de Django
#python manage.py runserver
ls
pwd
echo "npm run serve"
# Correr el servidor de Vue
cd ../aquaponics_vue 

npm run build 

# Esperar a que ambos procesos finalicen
#wait
