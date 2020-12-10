# Simple Mail Transfer Protocol (SMTP)
Analizamos el protocolo SMTP con una arquitectura cliente/servidor utilizando Dockers para así detectar posibles vulnerabilidades en el tráfico generado. Se realizó un video que muestra el tráfico generado y capturado con wireshark por la interacción entre el cliente y el servidor.

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
# Snort 
Para la captura de tráfico anómalo con snort, utilizamos las reglas que se ven en este [Archivo]

## Video de referencia con Snort. 

En este video se muestra como, utilizando Snort, logramos capturar paquetes con 5 tipos de reglas que creamos. [Video de youtube.](https://www.youtube.com/watch?v=Rek9CyL-1P8&feature=youtu.be&ab_channel=SergioLagos)
