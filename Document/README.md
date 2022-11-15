# integrador_ISP
Pasos para crear entorno virtual en local y lanzar el servidor django:

1) Crear entorno virtual:  py -m venv env
2) Activar entorno virtual: ./env/scripts/activate
3) Instalar los siguientes paquetes:
     pip install django 
     pip install mysqlclient
     pip install py mysql
     pip install djangorestframework

4) Crear BD en algún manejador de BD (ej: PHPmyAdmin)
5) Realizar las migraciones: py manage.py makemigrations 
6) Crear un superusuario: py manage.py createsuperuser
   Ingresar para el superusuario: (Nombre de usuario - Contraseña - E mail)
7) Levantar el servidor: py manage.py runserver

Listo!!
