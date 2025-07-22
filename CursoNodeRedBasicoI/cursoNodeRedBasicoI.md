# CURSO NODE-RED BÁSICO I

- [CURSO NODE-RED BÁSICO I](#curso-node-red-básico-i)
  - [¿Qué es Node-RED? ¿Cómo funciona? ¿Conceptos básicos?](#qué-es-node-red-cómo-funciona-conceptos-básicos)
  - [Instalación de Node-RED](#instalación-de-node-red)

---

## ¿Qué es Node-RED? ¿Cómo funciona? ¿Conceptos básicos?

Node-RED fue creado por IBM en el año 2013. Actualmente está liberado en GitHub con más de 600 nodos provenientes de la comunidad. Es una herramienta indispensable para el Internet de las cosas.

Node-RED está creado a partir de Node.js y se utiliza como un editor de flujos de datos y programación de funciones. Se utiliza principalmente en la industria 4.0 para la comunicación de datos y la interaccion con el mundo real.

Node-RED es accesible a través de un navegador web, y permite la programación orientada a eventos. Es un entorno de desarrollo de flujos de datos que permite crear, visualizar y administrar flujos de datos en tiempo real.

Node-RED está incluído en el sistema operativo Raspbian para la Raspberry Pi.

Los nodos se pueden clasificar en tres tipos:

- Nodos que solo admiten datos de entrada. Sirven para enviar datos a una base de datos o a un panel de control.
- Nodos que solo admiten datos de salida. Sirven para mostrar los datos a través de MQTT.
- Nodos que admiten tanto datos de entrada como de salida. Sirven para crear flujos de datos.

Los nodos se pueden interconectar entre sí mediante el curso, y realizar una tarea específica.

La propiedad principal es `payload` y se utiliza para enviar y recibir datos.

Se pueden realizar conexiones con: WebSocket, ThingSpeak, Google HOME, IFTTT, IBM Watson, etc.

En Node-RED se pueden usar protocolos de comunicación como: Modbus, MQTT, TCP, HTTP, Serial, FTP, etc.

Los flujos (_Flow_) se almacenan en el formato JSON y se pueden exportar a un archivo de texto o a un archivo de imagen.

## Instalación de Node-RED