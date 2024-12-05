# IoT con RBPi. Curso Avanzado

- [IoT con RBPi. Curso Avanzado](#iot-con-rbpi-curso-avanzado)
  - [Hardware en RBPi](#hardware-en-rbpi)
  - [Software en RBPi](#software-en-rbpi)
  - [Conexión a RBPi-3](#conexión-a-rbpi-3)

---

## Hardware en RBPi

- RBPi-3 modelo B o modelo B+.
- uSD, clase 10, 8 Gb
- Sensor temperatura DS1820.
- Sensor temperatura y presión BMP280.
- Sensor de movimiento por infrarrojo (PIR)
- Sensor magnético (para apertura de puertas)
- LEDs
- Módulo de Relay optoacoplado.
- Controlador PWM.

## Software en RBPi

- BalenaEtchar
- Win32 Disk Imager
- NMAP
- ZARC (es un ZIP)
- Notepad++
- PuTTY
- VNC Viewer
- TightVNC
- WinSCP (cliente FTP)
- FileZilla (cliente FTP)
- Raspbian Buster with Desktop

## Conexión a RBPi-3

La conexión se realizará desde la aplicación _PuTTY_ añadiendo la IP de la RBPi seleccionando SSH. La primera vez que nos conectamos, introducimos usuario y contraseña por defecto:

- login as: pi
- password: raspberry

Si queremos cambiar la contraseña usaremos el comando `passwd` seguido de la contraseña actual y luego la nueva.

Para configurar la RBPi `sudo raspi-config`. Tenemos varias opciones. Una opción que se debe activar es _VNC_.

La aplicación _VNC Viewer_ se instala en un PC con W10/11 nos permite conectarnos a la RBPi añadiendo la IP con el puerto por defecto 5900.
