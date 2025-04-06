''' Demonstrating GPIO input using logic switch
with event handler
Keith E. Kelly
4/10/21
'''
#import required libraries
import RPi.GPIO as GPIO
import time
from Buzzer import Buzzer

SWITCH_PIN = 19
BUZZER_PIN = 24

# # Configure GPIO setting
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(BUZZER_PIN, GPIO.OUT)
# GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.output(BUZZER_PIN, True)

# while True:
#     GPIO.output(BUZZER_PIN, GPIO.input(SWITCH_PIN))
#     time.sleep(.1)
# GPIO.cleanup()

buzzer = None

def switch_event_handler(channel):
    buzzer.toggle()

def pushbutton_init(pin:int):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=switch_event_handler)


def main():
    global buzzer
    pushbutton_init(SWITCH_PIN)
    buzzer = Buzzer(BUZZER_PIN)
    time.sleep(30)

if __name__ == "__main__":
    main()    
