#!/bin/sh
cd aquaponics_django
python manage.py migrate
python manage.py runserver &
cd ..
npm run serve
