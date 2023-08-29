'''piRover user blink 
Keith E. Kelly
8/24/20
'''
import time
import RPi.GPIO as GPIO

RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 18

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set specific pints as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Initialize all LEDs to OFF
GPIO.output(RED_PIN, False)
GPIO.output(GREEN_PIN, False)
GPIO.output(BLUE_PIN, False)

# user input
user_input = input("Which LED would you like to blink?")
color = user_input.upper()
if color == "RED":
    while True:
        GPIO.output(RED_PIN, True)
        time.sleep(1)
        GPIO.output(RED_PIN, False)
        time.sleep(1)
elif color == "GREEN":
    while True:
        GPIO.output(GREEN_PIN, True)
        time.sleep(1)
        GPIO.output(GREEN_PIN, False)
        time.sleep(1)
elif color == "BLUE":
    while True:
        GPIO.output(BLUE_PIN, True)
        time.sleep(1)
        GPIO.output(BLUE_PIN, False)
        time.sleep(1)
else:
    print("Sorry, that is not a valid pin.")
