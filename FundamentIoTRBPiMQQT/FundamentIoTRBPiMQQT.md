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
  - [Sección 4. Internet of Things](#sección-4-internet-of-things)
    - [Definición del término IoT](#definición-del-término-iot)
      - [Crear un dispositivo IoT](#crear-un-dispositivo-iot)
      - [Añadir Inteligencia Computacional](#añadir-inteligencia-computacional)
      - [Añadir conexión de red](#añadir-conexión-de-red)
    - [Dispositivos IoT vs Ordenadores en Red](#dispositivos-iot-vs-ordenadores-en-red)
    - [Tecnologías de IoT](#tecnologías-de-iot)
  - [Sección 5. Explicación del protocolo MQTT](#sección-5-explicación-del-protocolo-mqtt)
    - [Protocolo MQTT](#protocolo-mqtt)
      - [Publicador/Publisher](#publicadorpublisher)
      - [Suscriptor/Subscriber](#suscriptorsubscriber)
      - [Broker](#broker)
      - [Topic](#topic)
      - [Hostname](#hostname)
      - [Port](#port)
      - [Quality of Service (QoS)](#quality-of-service-qos)
    - [Broker MQTT en RBPi](#broker-mqtt-en-rbpi)
    - [Broker MQTT en distintas RBPi](#broker-mqtt-en-distintas-rbpi)
  - [Sección 6. IoT con Python y MQTT](#sección-6-iot-con-python-y-mqtt)
    - [Creando un publicador con Python y MQTT](#creando-un-publicador-con-python-y-mqtt)
      - [Crear un publicador](#crear-un-publicador)
    - [Creando un suscriptor con Python y MQTT](#creando-un-suscriptor-con-python-y-mqtt)
      - [Crear un suscriptor](#crear-un-suscriptor)
    - [Creando un chat con Python](#creando-un-chat-con-python)
    - [Control RBPi por línea de comandos](#control-rbpi-por-línea-de-comandos)
    - [Control RBPi por linea de comandos II](#control-rbpi-por-linea-de-comandos-ii)

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

---

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

---

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

---

## Sección 4. Internet of Things

### Definición del término IoT

Internet of Things (IoT) es una red de dispositivos conectados a Internet y que se comunican entre si.

- Internet: red interconectada de dispositivos para compartir información.
- Cosa: dispositivo capaz de realizar alguna cosa.

#### Crear un dispositivo IoT

Para convertir cualquier cosa en un dispositivo IoT, debemos tener en cuenta:

- Conectividad.
- Sensores.
- Actuadores.
- Procesamiento de datos.
- Almacenamiento de datos.
- Comunicación con otros dispositivos IoT.
- Seguridad.
- Escalabilidad.

#### Añadir Inteligencia Computacional

- Se hace con el fin de mejorar el funcionamiento de los dispositivos IoT.
- Se realiza con microcontroladores.

#### Añadir conexión de red

- Se amplian las posibilidades de comunicación de los dispositivos IoT.
- La manera más común es mediante la red WiFi.
- No se encuentra limitada a la red WiFi.
- Se puede crear una red propia.
- Las posibilidades son ilimitadas.

### Dispositivos IoT vs Ordenadores en Red

Un dispositivo IoT se diseña completamente diferente a una computadora convencional.

- Dispositivos IoT no tienen un sistema operativo.
- Dispositivos IoT no tienen un teclado y un ratón.
- Dispositivos IoT no tienen un monitor.
- Los dispositivos IoT son de propósito especial.
- El hasrware y el software son muy eficientes para una sola tarea.

Un PC tiene la función de realizar operaciones computacionales de cualquier tipo, es capaz de ejecutar cualquier tipo de programa.

- Las computadoras son de propósito general.
- Pueden realizar cualquier tarea.
- El hardware y el software son de propósito general.

### Tecnologías de IoT

Se implementan arquitecturas para IoT tipo: _AWS_, _Google Cloud_, _Microsoft Azure_, _IBM Bluemix_ y _IBM Watson IoT_.

El protocolo de comunicación de IoT se denomina _MQTT_ (Message Queuing Telemetry Transport).

---

## Sección 5. Explicación del protocolo MQTT

### Protocolo MQTT

El protocolo MQTT (Message Queuing Telemetry Transport) es un protocolo de comunicación ligero, disenado para la transmisión de mensajes en dispositivos IoT, especialmente aquellos con recursos limitados como memoria o ancho de banda.

- Es un protocolo basado en publicación y suscripción.
- Es considerado un protocolo de comunicación M2M (Machine-to-Machine).

Las colas de mensajes ofrecen un _buffer_ que almacena de forma temporal los mensajes enviados por el _publicador_ y que luego serán leidos por el _suscriptor_.

```mermaid
flowchart LR
   PRODUCER -- msg --> QUEUE -- msg --> CONSUMER
```

La estructura del protocolo MQTT es la siguiente:

```mermaid
flowchart LR
  PUBLICADOR:::foo -- topic --> BROKER:::bar -- topic --> SUSCRIPTOR:::foobar
  classDef foo stroke:#f00
  classDef bar stroke:#0f0
  classDef foobar stroke:#00f
```

- **Publicador**: Es el dispositivo que envía los mensajes.
- **Suscriptor**: Es el dispositivo que recibe los mensajes.
- **Broker**: Es el intermediario que distribuye los mensajes entre los publicadores y los suscriptores.
- **Cola de mensajes**: Es el buffer que almacena de forma temporal los mensajes enviados por el publicador y que luego serán leidos por el suscriptor.

#### Publicador/Publisher

- Se encarga de enviar la información (_payload_) al _broker MQTT_.
- Puede existir más de un publicador de manera simultánea.
- Existen muchas maneras de crear un publicador.
- Ejemplos para nombrar topics &rarr; `Topic=Casa/Cocina`.

#### Suscriptor/Subscriber

- Se encarga de recibir la información que llega desde el _broker MQTT_.
- Puede existir más de un suscriptor de manera simultánea.
- Existen muchas maneras de crear un suscriptor.
- La información no necesita ser validada antes de poder ser usada.

#### Broker

- Es el corazón de MQTT.
- Es un servidor encargado de recibir la información del _publicador_ y entregarla a los _suscriptores_.
- Es un intermediario entre los _publicadores_ y los _suscriptores_.
- El _broker_ más popular es _Mosquitto_.

#### Topic

- Es el canal de comunicación por donde el _publicador_ envía los datos y el _suscriptor_ los recibe.
- Es el nombre de la cola de mensajes. El nombre puede ser cualquiera.
- Si estamos usando diferentes _topic_ se usa la diagonal `/` para diferenciarlos.

![alt text](image.png "Diagrama de publicadores y suscriptores")

#### Hostname

- Es el equipo donde está instalado el _broker MQTT_.
- Si _hostname_ = `localhost` se usa el puerto 1883. El _broker_, el _publicador_ y el _suscriptor_ se encuentran en la misma maquina.
- Si _hostname_ = `127.0.0.1` se usa el puerto 1883. El _broker_, el _publicador_ y el _suscriptor_ se encuentran en la misma maquina.
- El _hostname_ puede usar otras direcciones IP.

#### Port

- El protocolo MQTT por defecto usa el puerto **1883**. Se puede cambiar en la configuración.

Para cambiar el puerto 1883 en MQTT, se debe modificar la configuración del broker MQTT. El puerto 1883 es el puerto predeterminado para la comunicación MQTT no segura. Para cambiarlo, localizar el archivo de configuración de broker `/etc/mosquitto/mosquitto.conf` y modifica la sección que define el puerto de escucha, generalmente 'port' o 'listener'. Después de modificar el archivo, se debe reiniciar el servicio Mosquitto.

Cambiar el valor del puerto al valor 8883 para MQTT seguro (**MQTT/TLS**).

#### Quality of Service (QoS)

Calidad de los servicios:

- **QoS 0**: Enviados sin garantía de entrega (_Fire and Forget_). Es el sistema más rápido
- **QoS 1**: Enviados con garantía de entrega (_At least once_). Se envía hasta que es reconocido por el _suscriptor_.
- **QoS 2**: Enviados con garantía de entrega y entrega inmediata (_Exactly once_). El _suscriptor_ y el _publicador_ estarán sincronizados para que una única copia es recibida.

### Broker MQTT en RBPi

Para instalar el _Broker MOSQUITTO_ a través de la terminal de la RBPi:

- `sudo apt-get update`.
- `sudo apt-get install mosquitto`.
- `sudo apt-get install mosquitto-clients`.

Para activar el servicio _Mosquitto_:

- `sudo systemctl start mosquitto`.
- `sudo systemctl status mosquitto`.
- `sudo systemctl enable mosquitto`.
- `sudo systemctl disable mosquitto`.
- `sudo systemctl restart mosquitto`.
- `sudo systemctl stop mosquitto`.
- `sudo systemctl reload mosquitto`.
- `sudo systemctl list-units --type=service --state=running | grep mosquitto`.
- `sudo systemctl list-units --type=service | grep mosquitto`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep loaded`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep disabled`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep active`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep inactive`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep failed`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep error`.
- `sudo systemctl list-units --type=service | grep mosquitto | grep unknown`.

Para suscribirse en el servicio _Mosquitto_:

- `mosquitto_sub -h localhost -v -t test -u MQTT -P MQTT`.
- `mosquitto_sub -h localhost -v -t test -u MQTT -P MQTT -q 1`.
- `mosquitto_sub -h localhost -v -t test -u MQTT -P MQTT -q 2`.
- `mosquitto_sub -h localhost -v -t test -u MQTT -P MQTT -q 0`.
- `mosquitto_sub -t casa/cocina`.

Para publicar en el servicio _Mosquitto_:

- `mosquitto_pub -h localhost -t test -m "hola mundo"`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT -r`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT -r -q 1`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT -r -q 2`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT -r -q 0`.
- `mosquitto_pub -h localhost -t test -m "hola mundo" -u MQTT -P MQTT -r -q 1 -d`.
- `mosquitto_pub -t casa/cocina -m "hola mundo"`.

### Broker MQTT en distintas RBPi

En RBPi:

- `mosquitto_sub -h IP-AQUI -t test/prueba`.

En PC con otro OS:

- `mosquitto_sub -h IP-AQUI -t test/prueba`.

En PC con servidor MQTT:

- `mosquitto_pub -t test/prueba -m "hola mundo"`.

---

## Sección 6. IoT con Python y MQTT

### Creando un publicador con Python y MQTT

En terminal de RBPi instalar: `pip3 install paho-mqtt` para Python 3. Si queremos en Python 2: `pip install paho-mqtt`.

#### Crear un publicador

```python
import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, result):
  print("Conexión exitosa")
  print("Client: {}\nUserdata: {}\nResult: {}".format(client, userdata, result))

if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"
  port = 1883
  topic = "test/prueba"
  contador = 0

  # declarar la instancia del cliente MQTT
  cliente = mqtt.Client()

  # asociar callbacks
  cliente.on_connect = on_publish

  # conectar con el broker
  cliente.connect(broker, port, keepalive=60)

  while True:
    # publicar un mensaje
    cliente.publish(topic, "hola mundo {}".format(contador))
    contador += 1
    time.sleep(1)

  # cerrar la conexión
  cliente.disconnect()
```

### Creando un suscriptor con Python y MQTT

En terminal de RBPi instalar: `pip3 install paho-mqtt` para Python 3. Si queremos en Python 2: `pip install paho-mqtt`.

#### Crear un suscriptor

```python
import paho.mqtt.client as mqtt
import time

# Esta función es llamada cuando se establece una conexión con el broker MQTT
def on_connect(client, userdata, flags, rc):
  print("Conexión con el código {}".format(rc))
  if rc == 0:
    print("Conexión exitosa")
  else:
    print("Conexión fallida")

# Esta función es llamada cuando se recibe un mensaje en el Topic
def on_message(client, userdata, msg):
  print("Mensaje recibido {}".format(msg.payload.decode("utf-8")))
  print("\n")
  print("Topic: {}".format(msg.topic))
  print("QoS: {}".format(msg.qos))
  print("Retain: {}".format(msg.retain))

if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"  # 192.168.x.x
  port = 1883
  topic = "test/prueba" # El tópico al que queremos suscribirnos

  # declarar la instancia del cliente MQTT
  cliente = mqtt.Client()

  # asociar callbacks
  cliente.on_connect = on_connect
  cliente.on_message = on_message

  # conectar con el broker
  cliente.connect(broker, port, keepalive=60)

  # suscribirse al Topic
  cliente.subscribe(topic)  # QoS es 0, se puede cambiar a 1 o 2
  """
  1. Simple string y un int: subscribe(topic, qos=1)
  2. Un diccionario: subscribe({topic: qos})
  3. Una lista de tuplas con varios topics: subscribe([(topic, qos), (topic, qos)])
  """
  # esperar mensajes
  cliente.loop_forever()

  # cerrar la conexión
  cliente.disconnect()
```

### Creando un chat con Python

En esta práctica se combina un _publicador_ y un _suscriptor_ en un mismo script Python.

```python
# PROGRAMA PARA PERSONA A
import paho.mqtt.client as mqtt
import time

FLAG = True

# Esta función es llamada cuando se establece una conexión con el broker MQTT
def on_connect(client, userdata, flags, rc):
  print("Conexión con el código {}".format(rc))
  if rc == 0:
    print("Conexión exitosa")
  else:
    print("Conexión fallida")

# Esta función es llamada cuando se recibe un mensaje en el Topic
def on_message(client, userdata, msg):
  global FLAG
  global mensaje
  respuesta = msg.payload.decode("utf-8")

  print("RESPUESTA {}".format(respuesta))

  if respuesta == "salir":
    FLAG = False
  else:
    mensaje = input("Introducir mensaje: ")
    mesaje = mensaje.lower()
    client.publish(topic_publisher, mensaje)

def on_subscribe(client, userdata, mid, granted_qos):
  print("Suscrito con QoS {}".format(granted_qos))

def on_unsubscribe(client, userdata, mid):
  print("Desuscrito")

def on_disconnect(client, userdata, rc):
  if rc != 0:
    print("Desconectado con el código {}".format(rc))

if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"  # 192.168.x.x
  port = 1883
  topic_publisher = "Chat/Cliente1" # El tópico al que queremos suscribirnos
  topic_subscriber = "Chat/Cliente2" # El tópico al que queremos suscribirnos

  # declarar la instancia del cliente MQTT
  cliente = mqtt.Client()

  # asociar callbacks
  cliente.on_connect = on_connect
  cliente.on_subscribe = on_subscribe
  cliente.on_unsubscribe = on_unsubscribe
  cliente.on_message = on_message
  #cliente.on_disconnect = on_disconnect

  # conectar con el broker
  cliente.connect(broker, port, keepalive=60)
  time.sleep(1)
  cliente.loop_start()

  # suscribirse al Topic
  cliente.subscribe(topic_subscriber)  # QoS es 0, se puede cambiar a 1 o 2
  time.sleep(1)

  mensaje = input("Introduzca el Mensaje a enviar para salir escibe<salir>: ")
  mensaje = mensaje.lower()

  # publicar un mensaje
  while FLAG:
    if mensaje == "salir":
      cliente.unsubscribe(topic_subscriber)
      cliente.disconnect()
      FLAG = False
    else:
      cliente.publish(topic_publisher, mensaje)
      mensaje = input("Introduzca el Mensaje a enviar para salir escibe<salir>: ")
      mensaje = mensaje.lower()

  # cerrar la conexión
  cliente.disconnect()
  cliente.loop_stop()
```

El siguiente script es el de la persona B:

```python
# PROGRAMA PARA PERSONA B
import paho.mqtt.client as mqtt
import time

FLAG = True

# Esta función es llamada cuando se establece una conexión con el broker MQTT
def on_connect(client, userdata, flags, rc):
  print("Conexión con el código {}".format(rc))
  if rc == 0:
    print("Conexión exitosa")
  else:
    print("Conexión fallida")

# Esta función es llamada cuando se recibe un mensaje en el Topic
def on_message(client, userdata, msg):
  global FLAG
  global mensaje
  respuesta = msg.payload.decode("utf-8")

  print("RESPUESTA {}".format(respuesta))

  if respuesta == "salir":
    FLAG = False
  else:
    mensaje = input("Introducir mensaje: ")
    mesaje = mensaje.lower()
    client.publish(topic_publisher, mensaje)

def on_subscribe(client, userdata, mid, granted_qos):
  print("Suscrito con QoS {}".format(granted_qos))

def on_unsubscribe(client, userdata, mid):
  print("Desuscrito")

def on_disconnect(client, userdata, rc):
  if rc != 0:
    print("Desconectado con el código {}".format(rc))

if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"  # 192.168.x.x
  port = 1883
  topic_publisher = "Chat/Cliente2" # El tópico al que queremos suscribirnos
  topic_subscriber = "Chat/Cliente1" # El tópico al que queremos suscribirnos

  # declarar la instancia del cliente MQTT
  cliente = mqtt.Client()

  # asociar callbacks
  cliente.on_connect = on_connect
  cliente.on_subscribe = on_subscribe
  cliente.on_unsubscribe = on_unsubscribe
  cliente.on_message = on_message
  #cliente.on_disconnect = on_disconnect

  # conectar con el broker
  cliente.connect(broker, port, keepalive=60)
  time.sleep(1)

  mensaje = None

  cliente.loop_start()

  # suscribirse al Topic
  cliente.subscribe(topic_subscriber)  # QoS es 0, se puede cambiar a 1 o 2
  # time.sleep(1)

  # mensaje = input("Introduzca el Mensaje a enviar para salir escibe<salir>: ")
  # mensaje = mensaje.lower()
  # publicar un mensaje
  # cliente.publish(topic_publisher, mensaje)
  
  while True:
    if (mensaje == "salir") or (FLAG == False):
      break

  # cerrar la conexión
  cliente.disconnect()
  cliente.loop_stop()
```

### Control RBPi por línea de comandos

Para este ejemplo se conecta el sensor de temperatura LM35 a la RBPi a través de un conversor ADC MCP3008. Por otro lado conectaremos un diodo LED al GPIO-17.

El código del lado del controlador (el usuario), sería el siguiente:

```python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

FLAG = True
#---------------------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
  print("Conexión con el código {}".format(rc))
#---------------------------------------------------------------------------------
def on_message(client, userdata, msg):
  global FLAG
  global mensaje
  respuesta = msg.payload.decode("utf-8")
  print("[TOPIC]: ", msg.topic)
  print("[RESPUESTA]: ", respuesta)

  if respuesta == "salir":
    FLAG = False
  else:
    mensaje = input("Introducir mensaje: ")
    mesaje = mensaje.lower()
    if mensaje == "on":
      topic = topics_publicar[0]
    elif mensaje == "off":
      topic = topics_publicar[0]
    elif mensaje == "temperatura":
      topic = topics_publicar[1]
    elif mensaje == "salir":
      topic = topics_publicar[1]
    client.publish(topic, mensaje)
#---------------------------------------------------------------------------------
def on_subscribe(client, userdata, mid, granted_qos):
  print("Suscrito con QoS {}".format(granted_qos))
#---------------------------------------------------------------------------------
def on_unsubscribe(client, userdata, rc):
  if rc != 0:
    print("Desconectado con el código {}".format(rc))
#---------------------------------------------------------------------------------
if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"  # 192.168.x.x
  port = 1883
  topics_publicar = ["Peticion/Luz", "Peticion/Temperatura"] # El tópico al que queremos suscribirnos
  topic_subscribir = [("Recamara/Luz",0), ("Recamara/Temperatura",0)] # El tópico al que queremos suscribirnos

  # declarar la instancia del cliente MQTT
  cliente = mqtt.Client()

  # asociar callbacks
  cliente.on_subscribe = on_subscribe
  cliente.on_unsubscribe = on_unsubscribe
  cliente.on_connect = on_connect
  cliente.on_message = on_message

  # conectar con el broker
  cliente.connect(broker, port, keepalive=60)
  time.sleep(0.1)

  cliente.loop_start()
  cliente.subscribe(topic_subscribir)  # QoS es 0, se puede cambiar a 1 o 2

  mensaje = input("Introduzca el Mensaje a enviar: ")
  mensaje = mensaje.lower()

  if mensaje == "on":
    topic = topics_publicar[0]
  elif mensaje == "off":
    topic = topics_publicar[0]
  elif mensaje == "temperatura":
    topic = topics_publicar[1]
  elif mensaje == "salir":
    topic = topics_publicar[1]
  
  cliente.publish(topic, mensaje)

  while True:
    if (mensaje == "salir") or (FLAG == False):
      break

  # cerrar la conexión
  cliente.disconnect()
  cliente.loop_stop()
```

### Control RBPi por linea de comandos II

Programa control de luces en Python y MQTT:

```python
import time
import paho.mqtt.client as mqtt
from gpiozero import LED, MCP3008

FLAG = True
mi_led = LED(17)
temperatura_actual = 0

def dame_temperatura():
  global temperatura_actual
  mi_adc = MCP3008(channel=0)
  while True:
    temperatura_actual = mi_adc.value*3.3*100
    return temperatura_actual

def on_connect(client, userdata, flags, rc):
  print("Conexión con el código {}".format(rc))

def on_message(client, userdata, msg):
  global FLAG
  global mensaje
  respuesta = message.payload.decode("utf-8")
  print("[TOPIC ORIGEN]: ", msg.topic)
  print("[RESPUESTA]: ", respuesta)
  if respuesta == "salir":
    FLAG = False
  elif respuesta == "on":
    mi_led.on()
    mensaje = "Luz encendida"
    topic = topics_publicar[0]
  elif respuesta == "off":
    mi_led.off()
    mensaje = "Luz apagada"
    topic = topics_publicar[0]
  elif respuesta == "temperatura":
    mensaje = dame_temperatura()
    mensaje = round(mensaje, 2)
    topic = topics_publicar[1]

  client.publish(topic, mensaje)

def on_subscribe(client, userdata, mid, granted_qos):
  print("Suscrito con QoS {}".format(granted_qos))

def on_unsubscribe(client, userdata, rc):
  if rc != 0:
    print("Desconectado con el código {}".format(rc))

if __name__ == "__main__":
  # broker al que queremos conectarnos
  broker = "localhost"  # 192.168.x.x
  port = 1883
  topics_publicar = ["Recamara/Luz", "Recamara/Temperatura"] # El tópico al que queremos suscribirnos
  topic_subscribir = [("Peticion/Luz",0), ("Peticion/Temperatura",0)] # El tópico al que queremos suscribirnos

  cliente = mqtt.Client()
  cliente.on_subscribe = on_subscribe
  cliente.on_unsubscribe = on_unsubscribe
  cliente.on_connect = on_connect
  cliente.on_message = on_message

  cliente.connect(broker, port, keepalive=60)
  time.sleep(0.1)
  mensaje = None

  cliente.loop_start()
  cliente.subscribe(topic_subscribir)  # QoS es 0, se puede cambiar a 1 o 2
  while True:
    if (FLAG == False) or (mensaje == "salir"):
      break
  cliente.disconnect()
  cliente.loop_stop()
```

Para probar el programa, desde el terminal ejecutamos el código del controlador: `python3 controlador.py`. Desde este programa, podemos apagar y encender la luz escribiendo `on`, `off`. Para saber el valor de la temperatura escribimos `temperatura`.

En una nueva terminal, ejecutar el programa que controla las luces de la RBPi: `python3 luces.py`.