#!/bin/sh
cd ../aquaponics_django
python manage.py migrate
python manage.py runserver &
cd ../aquaponics_vue
npm run serve
