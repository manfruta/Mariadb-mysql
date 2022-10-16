# Tarea N°1 ARQUITECTURAS DE ALTA DISPONIBILIDAD
Una simple Base de datos creada a partir de Dockerfiles uno cliente y otro servidor, con la finalidad de generar y capturar el trafico MySql que se genera entre ambos.

# La instalacion
Para construir el contenedor del servidor:
```
$ docker build -t mysql-server .
```
Para construie el contenedor del cliente:
```
$ docker build -t mysql-client2 -f Dockerfile.client .
```
Para contruir el contenedor del Polymorph:
```
$ docker build -t Polymorph -f Dockerfile.polymorph .
```

# Correr los contenedores



#### Acá lo importante es la opción –link server que permite la comunicación entre el cliente y el servidor

Correr el contenedor del servidor:
```
$ docker run -d  --name server mysql-server 
```
Correr el contenedor del cliente:
```
$ docker run -d --name client2 --link server mysql-client2
```
Correr el contenedor del Polymorph:
```
$ docker run --privileged -it <id de imagen>
```


# Lectura de trafico
Ahora se puede validar que haya tráfico entre cliente y servidor con el commando:
```
$ docker exec -it server tcpdump -i any -n -nn port 3306
```

# Muestra del trafico MySQL

#### https://www.youtube.com/watch?v=HI1-H4DpKX4&ab_channel=PlanA

# Muestra de modificación de trafico MySQL

#### https://www.youtube.com/watch?v=OH_bchaadh0&ab_channel=PlanA

#  Muestra  métricas de red  con protocolo MySQL

#### https://www.youtube.com/watch?v=A9SuWcVIwYM&ab_channel=Yeyoldo

# Muestra reglas Snort

#### https://www.youtube.com/watch?v=HcALnPp8ovE&ab_channel=Yeyoldo
