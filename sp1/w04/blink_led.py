'''piRover blink_led solution
Blinks external LED on breadboard
and integrated greenLED
Keith E. Kelly
9/16/25
'''
import time
import RPi.GPIO as GPIO

SHEADER_4 = 19
SHEADER_5 = 22
SHEADER_6 = 3   #Not Used

LED_EXT = SHEADER_4
LED_G = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_EXT, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

for i in range(0,10):
    print("turn the external LED on and green off")
    GPIO.output(LED_EXT, True)
    GPIO.output(LED_G, False)
    time.sleep(1)
    print("turn the external LED off and green on")
    GPIO.output(LED_EXT, False)
    GPIO.output(LED_G, True)
    time.sleep(1)

GPIO.cleanup()
  