# Source
# -------
# Dipto Pratyaksa
# http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/
import RPi.GPIO as GPIO
import time
import sys


def buzz(buzzer_pin, pitch, duration):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    if(pitch == 0):
        time.sleep(duration)
        return
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)

    for i in range(cycles):
        GPIO.output(buzzer_pin, True)
        time.sleep(delay)
        GPIO.output(buzzer_pin, False)
        time.sleep(delay)

if len(sys.argv) == 4:
    buzzer_pin = int(sys.argv[1])
    pitch = int(sys.argv[2])
    duration = float(sys.argv[3])

    buzz(buzzer_pin, pitch, duration)
    GPIO.cleanup()
else:
    print "python " + sys.argv[0] + " buzzer_pin pitch duration"
