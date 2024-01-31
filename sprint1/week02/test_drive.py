''' drive code to load the battery
for testing Rs
'''
import RPi.GPIO as GPIO
import time

PWMA	= 36    # left side
PWMB	= 33    # right side
AIN1	= 40
AIN2	= 38
BIN1	= 37
BIN2	= 35

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

# output pattern for forward motion
GPIO.output(AIN1, False)
GPIO.output(AIN2, True)
GPIO.output(BIN1, False)
GPIO.output(BIN2, True)

GPIO.output(PWMA, True)
GPIO.output(PWMB, True)


time.sleep(10)

GPIO.output(PWMA, False)
GPIO.output(PWMB, False)

time.sleep(1)