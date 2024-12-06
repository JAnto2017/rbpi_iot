import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

while True:
    if GPIO.input(17):
        print('Entrada ALTA')
    else:
        print('Entrada BAJA')
    time.sleep(1)  # esperar 1 s
    signal.signal(signal.SIGINT, signal_handler)

