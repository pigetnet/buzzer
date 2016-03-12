import RPi.GPIO as GPIO
import time
pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, True)
time.sleep(0.1)
GPIO.output(pin, False)

