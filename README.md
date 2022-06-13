# Simulador de Acuaponía
Simulador con el codigo fuente de simulador web para la construccion de un sistema de acuaponia.

## Instalación de frameworks, librerías y dependencias

### *Python*
- Version >= 3.7
- ***Django:*** >= 4.0

### *Node.js*
- Version >= 16.0
- ***Vue.js*** >= 5.0
- ***npm:*** >= 8.0

## Entorno virtual de Python

Crear, activar e instalar librerías necesarias

    pip install virtualenv
    virtualenv <nombre_venv>

Windows:

    <nombre_venv>\Script\activate
    
Linux/macOS:

    source bin/activate
    
Instalar librerías de Django

    pip install django, django-rest-framework, django-cors-headers
    
## Activar los servidores de desarrollo

***Python***

Abrir una nueva consola/terminal y ejecutar los siguientes comandos:

    cd <project_django>
    python manage.py runserver   

Abrir dirección URL en nuevo buscador: http://127.0.0.1:8000/admin

***Vue.js***

Abrir una nueva consola y ejecutar los siguientes comandos:

    npm install vue@next
    npm install -g @vue/cli
    
    cd <project_vue>
    
Librerías para Vue.js

    npm install axios
    npm install chart.js

Activar el servidor
    
    npm run serve

Abrir dirección URL en nuevo buscador: http://localhost:8080/
