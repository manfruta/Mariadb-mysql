
FROM ubuntu:latest
MAINTAINER Marcelo Luengo "marcelo.luengo@mail.udp.cl"
RUN apt-get update \
&& apt-get install -y locales  \
&& apt-get install -y mariadb-server \
&& apt-get install -y tcpdump \
&& rm -rf /var/lib/apt/lists/* \
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN mv /etc/mysql/mariadb.conf.d/50-server.cnf /tmp && \
sed 's/127.0.0.1/0.0.0.0/g' < /tmp/50-server.cnf > etc/mysql/mariadb.conf.d/50-server.cnf
RUN echo "CREATE USER 'root'@'%' IDENTIFIED BY 'root123';" >> /etc/mysql/init.sql && \
echo "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';" >> /etc/mysql/init.sql

EXPOSE 3306


CMD /usr/bin/mysqld_safe --init-file=/etc/mysql/init.sql


