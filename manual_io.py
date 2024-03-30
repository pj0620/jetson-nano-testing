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
    # set pin as an output pin with optional initial state of HIGH
    #for pin in pins:
    #    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
#    return

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.LOW
    try:
        while True:
            pin = int(input('enter pin to toggle: '))
            try:
                if pin not in pin_states:
                    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
                    pin_states[pin] = GPIO.HIGH 
                pin_states[pin] ^= GPIO.HIGH
                GPIO.output(pin, pin_states[pin])
            except:
                print('invalid pin')
    #        # Toggle the output every second
    #        for pin in pins:
    #            print("Outputting {} to pin {}".format(curr_value, pin))
    #            GPIO.output(pin, curr_value)
    #        curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
