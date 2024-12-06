import RPi.GPIO as GPIO
import signal
import time
import sys

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def signal_handler(sig, frame):
    GPIO.cleanup()
    print("Finalizando")
    sys.exit(0)

while True:
        print("Esperando")
        entrada = GPIO.wait_for_edge(pin, GPIO.FALLING, timeout=2000)
        if entrada is None:
            print("Tiempo excedido")
        else:
            print("Pulsador presionado")
        signal.signal(signal.SIGINT, signal_handler)
