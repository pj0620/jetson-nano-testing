import RPi.GPIO as GPIO

from utils import get_forward_pins, get_back_pins

GPIO.setmode(GPIO.BOARD)

for p in get_back_pins():
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(p, GPIO.LOW)

for p in get_forward_pins():
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(p, GPIO.HIGH)

GPIO.cleanup()
