import RPi.GPIO as GPIO

frecuencia
pwm = GPIO.PWM(canal, frecuencia)
pwm.start(dc)
pwm.ChangeFrequency(frecuencia)
pwm.ChangeDutyCycle(dc)
pwm.stop()