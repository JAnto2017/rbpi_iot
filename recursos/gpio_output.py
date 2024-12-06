import RPi.GPIO as GPIO
import sys

pin = int(sys.argv[1])
on_off = int(sys.argv[2])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, on_off)   