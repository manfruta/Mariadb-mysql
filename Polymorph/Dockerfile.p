FROM ubuntu
MAINTAINER Marcelo Luengo "marcelo.luengo@mail.udp.cl"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git net-tools iptables vim linux-modules-5.4.0-48-generic -y
RUN apt-get install kmod
RUN pip3 install git+https://github.com/kti/python-netfilterqueue\
&& pip3 install polymorph
