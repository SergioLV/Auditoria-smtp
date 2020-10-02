# Simple Mail Transfer Protocol (SMTP)
En esta tarea 2 del ramo Taller de Redes y Servicios, analizamos el protocolo SMTP con una arquitectura cliente/servidor utilizando Dockers para así detectar posibles vulnerabilidades en el tráfico generado. Se realizó un video que muestra el tráfico generado y capturado con wireshark por la interacción entre el cliente y el servidor y en este informe analizamos las posibles vulnerabilidades.

# Cliente
Para enviar mails al servidor, utilizamos la librería de python [Sender](https://github.com/SergioLV/sender)

## Instalación y ejecución.
Iniciamos con el comando docker build, el cual nos genera una imagen.
COMANNDO: docker build --rm -t sender .
Posteriormente con el comando docker image ls, obtendremos el ID de la imagen generada.
para luego con el comando docker run -it <ID> bash ingresar en nuestro docker.
# Servidor
Para ejecutar el servidor, utilizamos el software [Smtp4dev](https://github.com/rnwood/smtp4dev).

## Instalación y ejecucuón.
En el directorio del servidor, correr el comando docker run -p 3000:80 -p 2525:25 rnwood/smtp4dev:v3
