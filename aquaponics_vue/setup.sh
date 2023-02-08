#!/bin/sh
#cd ..
#npx browserslist@latest --update-db
#pip3 install -r requirements.txt

# Instalar pipenv
echo "instalando el ambiente virtual"
npm install --save-dev @vue/cli-service


# Crear entorno virtual con pipenv
#pipenv install

#apt install python3-pip python3-setuptools python3.8-venv
#sudo apt-get install python3-pip
pip install virtualenv 
virtualenv acuaponia-env

#python3 -m venv acuaponia-env --without-pip --system-site-packages

# Activar entorno virtual
#pipenv shell

# Realizar migraciones en la base de datos
cd ../aquaponics_django
python manage.py migrate

# Correr el servidor de Django
#python manage.py runserver
# Correr el servidor de Vue
cd ../aquaponics_vue
pwd
ls ./src

npm run build 


# Esperar a que ambos procesos finalicen
#wait
