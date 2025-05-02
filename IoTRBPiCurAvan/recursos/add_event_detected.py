import signal
import sys
import time
import RPi.GPIO as GPIO
PULSADOR = 17

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def button_pressed_callback(channel):
    print("Pulsador presionado")

GPIO.setmode(GPIO.BCM)
GPIO.setup(PULSADOR, GPIO.IN)
GPIO.add_event_detect(PULSADOR, GPIO.FALLING, callback=button_pressed_callback, bouncetime=100)
while True:
     print("Ejecutando resto del codigo")
     time.sleep(2)
     signal.signal(signal.SIGINT, signal_handler)
    