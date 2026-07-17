# CURSO NODE-RED BÁSICO I

- [CURSO NODE-RED BÁSICO I](#curso-node-red-básico-i)
  - [¿Qué es Node-RED? ¿Cómo funciona? ¿Conceptos básicos?](#qué-es-node-red-cómo-funciona-conceptos-básicos)
  - [Instalación de Node-RED](#instalación-de-node-red)
    - [Requisitos de la versión de Node.js](#requisitos-de-la-versión-de-nodejs)
    - [Instalación de Node-RED en Windows](#instalación-de-node-red-en-windows)
    - [Instalación de Node-RED en Ubuntu Server v24.04 (RBPi ARM64)](#instalación-de-node-red-en-ubuntu-server-v2404-rbpi-arm64)
    - [Resumen instalación Node-RED Node.js en Windows y Ubuntu Server v24.04 (RBPi ARM64)](#resumen-instalación-node-red-nodejs-en-windows-y-ubuntu-server-v2404-rbpi-arm64)

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

### Requisitos de la versión de Node.js

Node-RED (versión actual 5.0.1) recomienda Node.js (LTS) versión 24, siendo esta la versión sobre la que se construye las imágenes oficiales de Docker de Node-RED, y el mínimo absoluto soportado es Node.js 22.9.0, negándose Node-RED v5.0 a arrancar en versiones más antiguas.

No se recomienda usar versiones impares de Node.js, ya que no se prueban de forma rutinaria.

### Instalación de Node-RED en Windows

Paso 1: Instalar Node.js.

1. Descargar el instalador de Node.js v24 (LTS) desde la web [https://nodejs.org/es/download/](https://nodejs.org/es/download/).
2. Ejecutar el instalador. Puede ser con `.msi` o con `.exe`. Requiere permisos de administrador.
3. Al terminar de ejecutar el proceso se verá algo similar a: _node-red@1.0.0_ added 332 packages from 1 contributor_.
4. Verificar la instalación con el comando `node -v`.
5. Verificar la instalación con el comando `npm -v`.

Paso 2: Instalar Node-RED.

1. Descargar el instalador de Node-RED v5 desde la web [https://nodered.org/](https://nodered.org/).
2. Ejecutar el instalador. Puede ser con `.msi` o con `.exe`. Requiere permisos de administrador.
3. Al terminar de ejecutar el proceso se verá algo similar a: _node-red@1.0.0_ added 332 packages from 1 contributor_.
4. Acceder a la carpeta `C:\Program Files\node-red` y ejecutar el archivo `node-red.exe`.
5. Verificar la instalación con el comando `node-red -v`.
6. Acceder al navegador web con la URL: _`http://localhost:1880`_.

### Instalación de Node-RED en Ubuntu Server v24.04 (RBPi ARM64)

Se usa el script Pi, válido para Debian, Ubuntu y Raspbian. Se puede descargar de la web [https://github.com/node-red/node-red-pi](https://github.com/node-red/node-red-pi). Se ejecuta con el comando `sudo bash node-red-pi.sh`.

Opción A - Script oficial recomendada al instalar Node.js y Node-RED automáticamente:

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Este script:

- Detecta la arquitectura (ARM64).
- Instala o actualiza Node.js a la versión recomendada.
- Instala Node-RED y sus dependencias.
- Configura Node-RED para que se ejecute al arrancar el sistema (`systemd`).

Durante la ejecución preguntará si quieres:

- Instalar Node-RED-dashboard (opcional).
- Habilitar el arranque automático al iniciar el sistema.

Opción B - Instalación manual (más control sobre versiones)

1. Instalar Node.js v24.04 (LTS) desde repositirio oficial de NodeSource.
   1. `curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -`
   2. `sudo apt-get install -y nodejs`
2. Verificar versiones:
   1. `node -v`
   2. `npm -v`
3. Instalar Node-RED globalmente.
   1. `sudo npm install -g --unsafe-perm node-red`
4. Verificar la instalación con el comando `node-red -v`.
5. Acceder al navegador web con la URL: _`http://localhost:1880`_.
6. Configurar como servicio systemd para arranque automático:
   1. `sudo systemctl enable node-red.service`
   2. `sudo systemctl start node-red.service`
   3. `sudo systemctl status node-red.service`
   4. `sudo systemctl disable node-red.service`
   5. `sudo systemctl stop node-red.service`
   6. `sudo systemctl restart node-red.service`
   7. `sudo systemctl reload node-red.service`
   8. `sudo systemctl reset-failed node-red.service`
   9. `sudo systemctl daemon-reload`
7.  Compronación final. Al arrancar, la consola debe mostrar algo similar a: _node-red@1.0.0_ added 332 packages from 1 contributor_.

### Resumen instalación Node-RED Node.js en Windows y Ubuntu Server v24.04 (RBPi ARM64)

| App | Windows | Ubuntu (RBPi ARM64) |
| --- | --- | --- |
| Node.js | Instalador `.msi` desde nodejs.org | NodeSource repositorio |
| Node-RED | Instalador `.exe` desde nodered.org | Script oficial Pi o manual con npm |
| Arranque | Manual `node-red` | `systemd` (`nodered.service`) |
| Versión Node.js recomendada | 24.04 (LTS) | 24.04 (LTS) |