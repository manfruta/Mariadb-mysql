# Mariadb-mysql
Una simple Base de datos creada a partir de Dockerfiles uno cliente y otro servidor, con la finalidad de generar y capturar el trafico MySql que se genera entre ambos.

# La instalacion:
Para construir el contenedor del servidor:
```
$ docker build -t mysql-server .
```
Para construie el contenedor del cliente:
```
$ docker build -t mysql-client -f Dockerfile.client .
```


# Correr los contenedores:



#### Acá lo importante es la opción –link server que permite la comunicación entre el cliente y el servidor

Correr el contenedor del servidor:
```
$ docker run -d  --name server mysql-server 
```
Correr el contenedor del cliente:
```
$ docker run -d --name client --link server mysql-client
```


