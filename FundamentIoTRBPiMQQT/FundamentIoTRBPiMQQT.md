bb# Fundamentos IoT con RBPi. Comprende MQTT desde 0

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

## Sección 4. Explicación del IoT

## Sección 5. Explicación del protocolo MQTT

## Sección 6. IoT con Python y MQTT
