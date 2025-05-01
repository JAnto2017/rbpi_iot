# CURSO AUTOMATIZACIÓN E INTELIGENCIA ARTIFICIAL CON RBPi SCADA Y NODE-RED PROF24

- [CURSO AUTOMATIZACIÓN E INTELIGENCIA ARTIFICIAL CON RBPi SCADA Y NODE-RED PROF24](#curso-automatización-e-inteligencia-artificial-con-rbpi-scada-y-node-red-prof24)
  - [Módulo 1: Primeros pasos con RBPi](#módulo-1-primeros-pasos-con-rbpi)
    - [Características de la RBPi-4](#características-de-la-rbpi-4)
    - [Router configuración inicial](#router-configuración-inicial)
    - [Introducción IP's](#introducción-ips)
    - [Instalar Raspbian](#instalar-raspbian)
    - [Arrancando Raspbian en RBPi - Control remoto SSH](#arrancando-raspbian-en-rbpi---control-remoto-ssh)
      - [Comandos APT](#comandos-apt)
    - [Raspi-config y control VNC](#raspi-config-y-control-vnc)

---

## Módulo 1: Primeros pasos con RBPi

### Características de la RBPi-4

- Procesador ARM Cortex-A53 Quad Core
- 4 ó 8 GB de RAM LPDDR4
- 8 GB de almacenamiento en tarjeta microSD, clase 10
- Raspberry Pi 4 Model B o Raspberry Pi 4 Model B+
- Conector Ethernet 1Gbit
- x2 USB 2.0
- x2 USB 3.0
- X2 uHDMI resoluciones 1080p y 4K
- USB tipo C para la alimentación externa 5V/3A
- Puerto GPIO 40 pines
- Puerto I2C
- WiFi y Bluetooth

### Router configuración inicial

- Acceso al router a traves del navegador web: `http://192.168.1.1`
- Configuración de la zona horaria.
- Configuración de la clave de acceso a la red WiFi.

### Introducción IP's

- Cada dispositivo se interconecta a la red usando un número de IP.
- Un router tiene una IP pública para la conexión con otras redes.
- El router tiene una IP privada para la conexión con los dispositivos de la red privada o LAN.
- IP públicas y máscara de red. Ejemplo: `37.84.2.178/8`.
- IP privadas y máscara de red. Ejemplo: `220.178.44.111/24`.
- La _máscara de red_ determina el número de redes y de dispositivos que se pueden direccionar. Los bits que están a 1 lógico fijan las redes, por el contrario los bits a 0 fijan los dispositivos.
- IP públicas dinámicas, se pueden fijar a IP públicas estáticas, usando servicios en la web.

### Instalar Raspbian

- Utilizar el instalador _Raspberry Pi Imager v1.8.5_.
- Seleccionar el sistema operativo _Raspbian_ de 64 bits.
- Antes de iniciar el proceso de instalación pulsando sobre _Write_ se debe hacer clic sobre la configuración (icono en forma de rueda dentada)para configurar ciertos pasos importantes:
  - Enable SSH
    - Use password authentication
    - Allow public-key authentication
  - Set hostname
  - Set username and password
    - Username
    - Password
  - Configure wireless LAN
    - SSID
    - Password
    - Wireless LAN country: ES
  - Set locale settings
    - Time zone
    - Keyboard layout

### Arrancando Raspbian en RBPi - Control remoto SSH

- Conocer la IP de la RBPi una vez que está conectada con la herramienta NMAP.
- Usar la herramienta _putty_ para conectarse a la RBPi.
- Usar la herramienta _WinSCP_ para conectarse a la RBPi.
- Desde un terminal se puede acceder a la RBPi, escribiendo: `ssh pi@IP`.

#### Comandos APT

- _`sudo apt-get update`_. Variante: _`sudo apt update`_.
- _`sudo apt-get upgrade`_. Variantes: _`sudo apt upgrade`_, _`sudo apt full-upgrade`_.
- _`apt-cache search`_. Ejemplo: _`apt-cache search node`_. Muestra las versiones disponibles de un paquete.
- `apt-cache show node`. Muestra las características de un paquete.
- _`sudo apt-get install nodered`_. Variantes: _`sudo apt install nodered`_, _`sudo apt-get install node-red`_. Instalar sin confirmación de dependencias (_`-y`_).
- Para desinstalar: _`sudo apt-get purge nodered`_. Variantes: _`sudo apt purge nodered`_, _`sudo apt-get purge node-red`_. Desinstalar sin confirmación de dependencias (_`-y`_). Variante para desinstalar todos los paquetes: _`sudo apt-get remove`_.
- Para arreglar dependencias rotas: _`sudo apt-get -f install`_. Variantes: _`sudo apt -f install`_.
- Para actualizar todos los paquetes: _`sudo apt-get dist-upgrade`_. Variantes: _`sudo apt dist-upgrade`_.

### Raspi-config y control VNC