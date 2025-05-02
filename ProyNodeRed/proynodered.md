# Proyecto Node-RED Monitorización de Parámetros

- [Proyecto Node-RED Monitorización de Parámetros](#proyecto-node-red-monitorización-de-parámetros)
  - [Sección 1 - Introducción y Presentación del Proyecto](#sección-1---introducción-y-presentación-del-proyecto)
  - [Sección 2 - Desarrollo del Proyecto](#sección-2---desarrollo-del-proyecto)
    - [Creando el apartado de Información](#creando-el-apartado-de-información)
    - [Creando el apartado de Alamacenamiento](#creando-el-apartado-de-alamacenamiento)

- - -

## Sección 1 - Introducción y Presentación del Proyecto

Creación de un _Dashboard_ para monitorear parámetros del sistema operativo en la Raspberry Pi, tales como:

- Uso de CPU
- Temperatura
- Almacenamiento:
  - Total
  - Disponible
  - Usado
- Memoria RAM
- Velocidad del procesador
- Hostname
- IP Address
- Fecha y hora

## Sección 2 - Desarrollo del Proyecto

### Creando el apartado de Información

Accedemos a Node-RED en la URL: `http://192.168.0.41:1880/`.

- Añadir nombre, hacer doble clic en la pestaña _Flow 1_.
- ![alt text](image.png "Nombre del Flow")

Para cumplimentar el siguiente paso, se debe hacer clic en el icono y localizar la opción _Dashboard_. Tal y como se indica en la imagen:

![alt text](image-10.png "Opción Dashboard")

Siguiente paso, es crear una pestaña (_TAB_) con tres grupos dentro.

- ![alt text](image-1.png "Pestaña nueva con igual nombre")
- ![alt text](image-2.png "Pestaña con tres grupos dentro")
- ![alt text](image-3.png "Características de la pestaña")
- ![alt text](image-4.png "Objetivo final de la pestaña con los tres grupos")

En los componentes _dashboard_ que están disponibles lado izquierdo, buscar el _text_ y añadirlo al _Flow_:

- ![alt text](image-5.png "Añadir componente _text_")
- ![alt text](image-6.pngb "Configuración del componente _text_")

Siguiente paso es añadir tres nodes _text_: Hostname, IP Address y Fecha y Hora.

- Comando para saber el hostname de la RBPi: `hostnamectl | grep hostname` o simplemente escribiendo `hostname`. El módulo que utilizaremos es _exec_ que sirve para ejecutar comandos de sistema.
- El módulo _exec_ lo ejecutaremos con un nodo _inject_ que es el que indica cuándo ejecutar el comando.
- ![alt text](image-7.png "Conexión módulo inject con el nodo text")
- ![alt text](image-8.png "Configuración del módulo inject")
- La salida del _exec_ lo conectaremos al nodo _text_.
- ![alt text](image-9.png "Configuración del nodo _text_")
- Para saber la IP de la RBPi, usaremos el módulo _exec_ con el comando `hostname -I`. El módulo _exec_ lo ejecutaremos con un nodo _inject_ que es el que indica cuándo ejecutar el comando.
- ![alt text](image-11.png "Configuración del nodo _text_")
- Para saber la fecha y hora, usaremos el módulo _exec_ con el comando `date`. El módulo _exec_ lo ejecutaremos con un nodo _inject_ que es el que indica cuándo ejecutar el comando.
- En este caso el node _inject_ lo configuramos para que se ejecute cada segundo.
- ![alt text](image-12.png "Configuración del nodo _inject_")
- ![alt text](image-13.png "Configuración del nodo _text_")

Para realizar una distribución de los componentes en el _Dashboard_, podemos hacer clic en el icono y localizar la opció _Layout_. Tal y como se indica en la imagen:

- ![alt text](image-14.png "Opción Layout en Monitorización con RBPi")
- ![alt text](image-15.png "Vista acabada del _Dashboard_")

### Creando el apartado de Alamacenamiento