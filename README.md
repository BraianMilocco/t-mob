# t-mob
ejercicio

# Descripción
Ejercicio de entrevista técnica.
- Generar modelo de Redirect
- Generar vista por GET con key como parámetro que devuelva un json {'key':[key],'url':[url] 
- Recuperar los datos a devolver en la view usando memcached
- Generar Signal que guarde los Redirect activos en la memcached cada vez que se genera una modificación en alguno

### Consideraciones
Para la signal dejé dos opciones, una comentada y otra en funcionamiento. A continuación explico las variantes:
 - funcionando: Cuando se crea/edita/borra un Redirect, se borra la caché, se recuperan todos los Redirect con active == True y se los guarda en la caché
- Comentada: Cuando se crea/edita/borra un redirect, se saca esa la key de la caché, y si se vuelve a buscar la instancia para agregarla nuevamente (si se encuentra activa)

En caso de que la key que se pase por parámetro no se encuentre activa o no exista, se tira un 404 por defecto

## Requisitos

- pip3 
```bash
sudo apt-get install python3-pip
```
- virtualenv 
```bash
pip3 install virtualenv
```
- [mysql server](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es)
- [memcached](https://memcached.org/downloads)

## Instalación
 - crear carpeta del proyecto, ingresar a la misma
 - iniciar git 
```bash
git init
```
 - clonar repositorio
```bash
git clone https://github.com/BraianMilocco/t-mob.git
```
 - crear virtual enviroment
```bash
python3 -m venv
```
 - iniciar venv ()
```bash
source venv/bin/activate
``` 
- instalar dependencias (pip3 install -r requirements.txt)
```bash
pip3 install requirements.txt
```
- configurar mysql
```bash
sudo systemctl start mysql
sudo systemctl enable mysql
sudo mysql -u root -p
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE tmob;
USE tmob;
GRANT ALL PRIVILEGES ON tmob.* TO 'user'@'localhost';
```

- Generar Migraciones
```bash
python3 manage.py makemigrations
```
- Migrar DB
```bash
python3 manage.py migrate
```
- Crear Super Usuario
```bash
python3 manage.py createsuperuser
```
## Correr
- Correr server
```bash
python3 manage.py runserver
```

#### urls
 - admin: http://127.0.0.1:8000/admin
 - api: http://127.0.0.1:8000/api/redirect/{key}
