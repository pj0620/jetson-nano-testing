import RPi.GPIO as GPIO
import time

#GPIO.cleanup()

# Pin Definitions
#pins = [37, 33]  # BOARD pin 12, BCM pin 18
#pins = [12, 76, 38, 200]

pin_states = {}

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    # set pin as an output pin with optional initial state of HIGH
    #for pin in pins:
    #    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
#    return

    print("Starting demo now! Press CTRL+C to exit")
    #curr_value = GPIO.LOW
    for pin in range(50):
        try:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
            print('turning off ' + str(pin))
            GPIO.output(pin, GPIO.LOW)
            time.sleep(2)
            print('turning on ' + str(pin))
#            GPIO.output(pin, GPIO.HIGH)
 #           time.sleep(2)
            print('turning off ' + str(pin))
  #          GPIO.output(pin, GPIO.LOW)
   #         time.sleep(2)
        except Exception as e:
            print('pin ' + str(pin) + ' is invalid', e)
    GPIO.cleanup()

if __name__ == '__main__':
    main()
