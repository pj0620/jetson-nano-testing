import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins_back = [26, 22, 35, 31]
pins_forward = [24, 37, 23, 33]

for p in pins_back:
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(p, GPIO.LOW)
    
for p in pins_forward:
    GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for p in pins_forward:
            GPIO.output(p, GPIO.HIGH)
        time.sleep(0.01)
        for p in pins_forward:
            GPIO.output(p, GPIO.LOW)
        time.sleep(0.01)
finally:
    GPIO.cleanup()
