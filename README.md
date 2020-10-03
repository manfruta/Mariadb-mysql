# Mariadb-mysql
Una simple Base de datos creada a partir de Dockerfiles uno cliente y otro servidor, con la finalidad de generar y capturar el trafico MySql que se genera entre ambos.

# La instalacion:
Para construir el contenedor del servidor:
$ docker build -t mysql-server .

Para construie el contenedor del cliente:

$ docker build -t mysql-client -f Dockerfile.client .



### postgres Version



#### Obtencion de ip del contenedor de docker



estoy pal pico `frodenas/postgresql`


$ docker run -d --name postgresql -p 5432:5432 frodenas/postgresql

variables:

* `POSTGRES_USERNAME` to set a specific username
* `POSTGRES_PASSWORD` to set a specific password
