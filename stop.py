import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins_back = [24, 23, 35, 31]
pins_forward = [22, 37, 26, 33]

for p in pins_back:
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(p, GPIO.LOW)

for p in pins_forward:
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(p, GPIO.LOW)

GPIO.cleanup()
