# Documentacion para instalacion de prueba para Asignado

## Para Frontend
1. Se debe instalar el [cli de ember](https://emberjs.com), el cual funciona con [npm](https://www.npmjs.com/get-npm?utm_source=house&utm_medium=homepage&utm_campaign=free%20orgs&utm_term=Install%20npm)
2. Se ingresa en una terminal, se dirige a la carpeta frontend/activos y se ejecutan los comandos:
```
npm install
ember serve --environment=development
```

## Para Backend
1. Se debe instalar [python3](https://www.python.org/downloads/)
2. Luego se instala desde una terminal python-virtualenv con el comando:
```
pip install python-virtualenv
```
3. Ahora se crea un entorno virtual y se activa:
```
virtualenv activos
source /<ruta>/activos/bin/activate
```
4. Instalamos las dependencias del proyecto:
```
pip install -r requirements.txt
```
5. Instalamos [postgres](https://www.postgresql.org/) y [postgis](http://postgis.net/)
6. Se crea una base de datos, se le agrega la extension de postgis (CREATE EXTENSION postgis;) y se crea un usuario con permisos sobre la base de datos.
7. Ahora editamos el archivo postactivate del entorno virtual y editamos las variables con los respectivos datos
export SECRET_KEY=(adjunto en el correo)
export NAME=
export USER=
export PASSWORD=
export HOST=
export PORT=
8. Aplicamos las migraciones en la base de datos
```
./manage.py migrate
```
9. Creamos un super usuario para el admin de django e ingresamos los datos solicitados (usuario, correo y password)
```
./manage.py createsuperuser
```
10. Corremos el proyecto
```
./manage.py runserver
```

### Nota: La url para el frontend [http://127.0.0.1:4200] y la del backend es [http://127.0.0.1:8000]
