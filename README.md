# Mariadb-mysql
Una simple Base de datos creada a partir de Dockerfiles uno cliente y otro servidor, con la finalidad de generar y capturar el trafico MySql que se genera entre ambos.

# La instalacion:
Para construir el contenedor del servidor:
```
$ docker build -t mysql-server .
```
Para construie el contenedor del cliente:
```
$ docker build -t mysql-client2 -f Dockerfile.client .
```


# Correr los contenedores:



#### Acá lo importante es la opción –link server que permite la comunicación entre el cliente y el servidor

Correr el contenedor del servidor:
```
$ docker run -d  --name server mysql-server 
```
Correr el contenedor del cliente:
```
$ docker run -d --name client2 --link server mysql-client2
```

# Lectura de trafico
Ahora se puede validar que haya tráfico entre cliente y servidor con el commando:
```
$ docker exec -it server tcpdump -i any -n -nn port 3306
```
