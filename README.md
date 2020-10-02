# Simple Mail Transfer Protocol (SMTP)
En esta tarea 2 del ramo Taller de Redes y Servicios, analizamos el protocolo SMTP con una arquitectura cliente/servidor utilizando Dockers para así detectar posibles vulnerabilidades en el tráfico generado. Se realizó un video que muestra el tráfico generado y capturado con wireshark por la interacción entre el cliente y el servidor y en este informe analizamos las posibles vulnerabilidades.

# Servidor
Para ejecutar el servidor, utilizamos el software [Smtp4dev](https://github.com/rnwood/smtp4dev).

## Instalación y ejecución.
Para levantar el Docker del servidor y que reciba correos en el puerto 2525, simplemente se ejecuta el comando:
```sh
docker run -p 3000:80 -p 2525:25 rnwood/smtp4dev:v3
```
y ready-to-go!

# Cliente
Para enviar mails al servidor, utilizamos la librería de python [Sender](https://github.com/SergioLV/sender)

## Instalación y ejecución.
Para generar una imagen de Docker para el cliente, iniciamos con el comando:
```sh
docker build --rm -t sender .
```
Luego,
```sh
docker image ls
```
para obtener el id del contenedor.

Posteriormente,
```sh
docker run -it <ID> bash
```
para ingresar al contenedor.

Finalmente,
```sh
python3 sender.py 
```
para enviar un correo con datos al servidor y luego un correo con una imagen.
