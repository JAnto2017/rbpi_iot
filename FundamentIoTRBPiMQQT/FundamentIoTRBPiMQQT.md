# Fundamentos IoT con RBPi. Comprende MQTT desde 0

- [Fundamentos IoT con RBPi. Comprende MQTT desde 0](#fundamentos-iot-con-rbpi-comprende-mqtt-desde-0)
  - [Sección 1. Introducción](#sección-1-introducción)
  - [Conocimientos Previos](#conocimientos-previos)
    - [Terminal de Linux](#terminal-de-linux)
    - [Programación en Python](#programación-en-python)
    - [Hardware](#hardware)
  - [Sección 2. Funcionamiento de Internet](#sección-2-funcionamiento-de-internet)
    - [Bit \& Byte](#bit--byte)
    - [Conexiones a Internet](#conexiones-a-internet)
    - [Direcciones IP](#direcciones-ip)
    - [Puertos de Red](#puertos-de-red)
    - [DNS](#dns)
    - [Protocolos de Internet](#protocolos-de-internet)
  - [Sección 3. Modelo Cliente-Servidor](#sección-3-modelo-cliente-servidor)
    - [Modelos Cliente - Servidor](#modelos-cliente---servidor)
    - [Sockets](#sockets)
      - [Socket del Cliente](#socket-del-cliente)
      - [Socket del Servidor](#socket-del-servidor)
    - [Servidor con Python](#servidor-con-python)
    - [Cliente con Python](#cliente-con-python)
    - [Cliente y Servidor en distintos Equipos](#cliente-y-servidor-en-distintos-equipos)
  - [Sección 4. Explicación del IoT](#sección-4-explicación-del-iot)
  - [Sección 5. Explicación del protocolo MQTT](#sección-5-explicación-del-protocolo-mqtt)
  - [Sección 6. IoT con Python y MQTT](#sección-6-iot-con-python-y-mqtt)

---

## Sección 1. Introducción

Fundamentos IoT con RBPi.

## Conocimientos Previos

### Terminal de Linux

- Moverse entre directorios.
- Ejecutar scripts en Python desde terminal.
- Instalar paquetes en Terminal.

### Programación en Python

- Fundamentos de programación.
- Programación orientada a objetos.
- Módulo TKinter.

### Hardware

- Módulo _gpiozero_.
- Circuitos en protoboard.
- Cómo funciona un ADC (C.I. MCP3008 de 10 bits).
- Sensores.

## Sección 2. Funcionamiento de Internet

### Bit & Byte

- Un bit es un dato de 0 o 1. Mínima cantidad de información.
- Un byte es compuesto de 8 bits. Se cuenta desde el bit 0 hasta el 7.

La tabla ASCII asocia un valor decimal representado en binario a cada símbolo del alfabeto. Ejemplos:

- `@` = 64 = 0100 0000
- `A` = 65 = 0100 0001
- `ñ` = 164 = 1010 0001
- `Ñ` = 165 = 1010 0010

### Conexiones a Internet

El servicio DHCP otorga direcciones IP diferentes de forma dinámica a cada dispositivo conectado a a red.

### Direcciones IP

**IP** proviene de las siglas _Internet Protocolo_. Estas direcciones de 32 bitspermiten identificar un dispositivo dentro de una red.

- IP _localhost_: 127.0.0.1

### Puertos de Red

Son canales de información por los cuales, en cada uno de ellos viaja información muy específica con características bien definidas.

Los protocolos más populares de Internet son:

- HTTP (HyperText Transfer Protocol). Canal 80.
- HTTPS (HyperText Transfer Protocol Secure). Canal 443.
- SMTP (Simple Mail Transfer Protocol). Canal 25.
- DNS (Domain Name System). Canal 53.
- MQTT (Message Queue Telemetry Transport). Canal 1883.
- UDP (User Datagram Protocol). Canal 53.
- TCP (Transmission Control Protocol). Canal 23.
- ICMP (Internet Control Message Protocol). Canal 1.
- IGMP (Internet Group Management Protocol). Canal 2.

> [!NOTE]
>
> En total existen **65.536** puertos.</br>
> Para direccionarlos se usan 2 bytes.</br>
> $ 2^{16} = 65.536 $</br>

### DNS

**DNS** _Domain Name System_. Se usa para traducir nombres de dominio a direcciones IP.

Son un grupo de servidores con una base de datos de nombres de dominio. Ello permite relacionar la dirección IP pública con un nombre de dominio.

- `ping google.com` &rarr; ping a google.com muestra la dirección IP.
- `nslookup google.com` &rarr; muestra la información de google.com.

### Protocolos de Internet

Un protocolo es un conjunto de reglas que permiten la comunicación entre dos dispositivos. Estas reglas deben especificar: cómo deben transferirse los datos y que datos deben estar en cada paquete.

- TCP (Transmission Control Protocol). Canal 23.
- UDP (User Datagram Protocol). Canal 53.
- MQTT (Message Queue Telemetry Transport). Canal 1883.
- HTTP (HyperText Transfer Protocol). Canal 80.
- HTTPS (HyperText Transfer Protocol Secure). Canal 443.

## Sección 3. Modelo Cliente-Servidor

### Modelos Cliente - Servidor

El modelo cliente-servidor está basado en la comunicación bidireccional entre dos dispositivos.

```mermaid
flowchart LR
    Cliente-->|peticiones|Servidor
```

```mermaid
flowchart LR
    Servidor-- respuestas -->Cliente
```

> [!NOTE]
> El Cliente realiza peticiones al servidor.
> El Servidor responde a las peticiones del cliente.

### Sockets

Un socket es un punto de comunicación entre dos dispositivos. Puede ser un socket TCP o un socket UDP.

#### Socket del Cliente

1. Crear el socket.
2. Conectar el socket al servidor.
3. Enviar mensajes (_request_).
4. Recibir mensajes (_response_).
5. Cerrar el socket.

#### Socket del Servidor

1. Crear el socket.
2. Enlazar el socket con un puerto y una dirección IP.
3. Escuchar por una conexión.
4. Aceptar la conexión
5. Recibir mensajes (_request_).
6. Enviar mensajes (_response_).
7. Cerrar el socket.

### Servidor con Python

Archivo `server.py`:

```python
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.running = True

    def start(self):
        while self.running:
            client, address = self.server.accept()
            self.clients.append(client)
            thread = Thread(target=self.handle, args=(client,))
            thread.start()

    def handle(self, client):
        while self.running: 
            msg = client.recv(1024)
            for c in self.clients:
                c.send(msg) 

    def stop(self):
        self.running = False
        self.server.close()
        for c in self.clients:
            c.close() 
```

Ejemplo de servidor en Raspberry Pi:

```python
import socket

if __name__ == "__main__":
    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    servidor = socket.gethostname(socket.gethostname())
    # Enlazar el socket con un puerto y una direccion IP
    s.bind((servidor, 1234))
    # Escuchar por una conexion
    s.listen(5) # El argumento indica la cantidad de conexiones pendientes
    # Aceptar la conexion
    while True:
        conexion, direccion = s.accept()
        print("Conexion con {} ha sido establecida ".format(direccion))
        # Aceptar request
        respuesta = conexion.recv(1024)
        if not respuesta:
            break
        print("Mensaje recibido: {}".format(respuesta.decode("utf-8")))
        print("\n")
        # Enviar response
        conexion.send(byte("Recibido","utf-8"))
    
    # Cerrar la conexion
    conexion.close()
    s.close()
```

Para probar el servidor podemos ejecutar el archivo `python3 server.py` en la terminal de Linux.

### Cliente con Python

Archivo `client.py`:

```python
import socket 

if __name__ == "__main__":
    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname(socket.gethostname())
    
    # Conectar el socket al servidor  
    s.connect((host, 1234)) # 1234 es el puerto genérico
    
    # Enviar request  
    mensaje = input("Introduzca el Mensaje a enviar: ")
    s.send(byte(mensaje, "utf-8"))
    
    # Recibir response
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8"))
    
    # Cerrar la conexion
    s.close()
```

Para probar el cliente podemos ejecutar el archivo `python3 client.py` en la terminal de Linux. El servidor debe estar funcionando.

### Cliente y Servidor en distintos Equipos

En los programas anteriores se deben cambiar las direcciones IP. Si ejecutamos el servidor en la RBPi y el cliente en la PC, debemos cambiar la IP del servidor por la IP de la RBPi.

Programa del cliente:

```python
import socket

if __name__ == "__main__":
    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "89.0.142.86" # Dirección IP del servidor
    # Conectar el socket al servidor  
    s.connect((host, 1234)) # 1234 es el puerto genérico
    # Enviar request  
    mensaje = input("Introduzca el Mensaje a enviar: ")
    s.send(byte(mensaje, "utf-8"))
    # Recibir response
    respuesta = s.recv(1024)
    print(respuesta.decode("utf-8"))
    # Cerrar la conexion
    s.close()
```

Programa del servidor:

```python
import socket

if __name__ == "__main__":
    # Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = socket.gethostname(socket.gethostname())
    servidor = "0.0.0.0"
    
    # Enlazar el socket con un puerto y una direccion IP
    s.bind((servidor, 1234))
    
    # Escuchar por una conexion
    s.listen(5) # El argumento indica la cantidad de conexiones pendientes
    
    # Aceptar la conexion
    while True:
        conexion, direccion = s.accept()
        print("Conexion con {} ha sido establecida ".format(direccion))
        
        # Aceptar request
        respuesta = conexion.recv(1024)
        if not respuesta:
            break
        print("Mensaje recibido: {}".format(respuesta.decode("utf-8")))
        print("\n")
        
        # Enviar response
        conexion.send(byte("Recibido","utf-8"))
    
    # Cerrar la conexion
    conexion.close()
    s.close()
```

Para controlar el LED en el PIN-17 de la RBPi en el código del servidor, añadiremos el siguiente código:

```python
import gpiozero import LED

while True:
  # creamos instancia del LED
  led = LED(17)

  # aceptar conexión

  # Aceptar request
  datos = conexion.recv(1024)

  # código del LED
  if datos.decode("utf-8") == "ON":
    led.on()
  elif datos.decode("utf-8") == "OFF":
    led.off() 
```

Tras iniciar el servidor, si desde el cliente se envía el mensaje "ON" se encenderá el LED. Si se envía el mensaje "OFF" se apagará el LED. En el caso de que se envíe otra cosa, el LED no se encenderá ni se apagará.

## Sección 4. Explicación del IoT

## Sección 5. Explicación del protocolo MQTT

## Sección 6. IoT con Python y MQTT
