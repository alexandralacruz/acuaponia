#!/bin/sh
#cd ..
#npx browserslist@latest --update-db
#pip3 install -r requirements.txt
#pip3 install virtualenv 
echo "instalando el ambiente virtual"

virtualenv acuaponia-env
. acuaponia-env/bin/activate
echo $VIRTUAL_ENV

pip3 install -r requirements.txt
npx browserslist@4.21.5 
# Instalar pipenv
npm install --save-dev @vue/cli-service


# Crear entorno virtual con pipenv
#pipenv install

#apt install python3-pip python3-setuptools python3.8-venv
#sudo apt-get install python3-pip


#python3 -m venv acuaponia-env --without-pip --system-site-packages

# Activar entorno virtual
#pipenv shell

# Realizar migraciones en la base de datos
cd ..
cd aquaponics_django
#python manage.py migrate
ls
python manage.py runserver &

# Correr el servidor de Django
#python manage.py runserver
# Correr el servidor de Vue
cd ..
cd aquaponics_vue
pwd

npm run build 


# Esperar a que ambos procesos finalicen
#wait
