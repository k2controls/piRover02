''' piRover Drive 
Contains GPIO function to control piRover drive.

Keith E. Kelly
11/19/20
'''
import RPi.GPIO as GPIO

L_PWM = 36
R_PWM = 33
L_IN1 = 40
L_IN2 = 38
R_IN1 = 37
R_IN2 = 35

left_speed = None
right_speed = None

DEFAULT_SPEED = 50
DELTA_SPEED = 5
speed_value = DEFAULT_SPEED

def drive_init():
    global left_speed, right_speed

    #print("Initializing the GPIO ports supporting drive ops.")
    #Configure GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    #set MC pins as output
    GPIO.setup(L_IN1, GPIO.OUT, initial = False)
    GPIO.setup(L_IN2, GPIO.OUT, initial = False)
    GPIO.setup(R_IN1, GPIO.OUT, initial = False)
    GPIO.setup(R_IN2, GPIO.OUT, initial = False)
  
    # set enable pins as output
    GPIO.setup(L_PWM, GPIO.OUT, initial = True)
    GPIO.setup(R_PWM, GPIO.OUT, initial = True)

    left_speed = GPIO.PWM(L_PWM, 50)
    right_speed = GPIO.PWM(R_PWM, 50)
    left_speed.start(DEFAULT_SPEED)
    right_speed.start(DEFAULT_SPEED)

def forward():
    #print("you are going forward...")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, True)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, True)

def backward():
    #print("you are going backward...")
    GPIO.output(L_IN1, True)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, True)
    GPIO.output(R_IN2, False)
    
def left_forward():
    #print("you are turning left forward...")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, True)

def left_rotate():
    #print("you are rotating left...")
    GPIO.output(L_IN1, True)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, True)

def left_backward():
    #print("you are turning left backward...")
    GPIO.output(L_IN1, True)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, False)

def right_forward():
    # print("you are turning right forward...")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, True)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, False)

def right_rotate():
    # print("you are rotating right...")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, True)
    GPIO.output(R_IN1, True)
    GPIO.output(R_IN2, False)

def right_backward():
    # print("you are turning right backward...")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, True)
    GPIO.output(R_IN2, False)

def stop():
    #print("you are stopped.")    
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, False)

def accelerate():
    global speed_value, left_speed, right_speed
    if speed_value < 100:
        #print("you are accelerating...")
        speed_value = speed_value + DELTA_SPEED
        left_speed.ChangeDutyCycle(speed_value)
        right_speed.ChangeDutyCycle(speed_value)
#    print(f"Current speed is {speed}.")

def decelerate():
    global speed_value, left_speed, right_speed
    if speed_value > 0:
        # print("you are decelerating...")
        speed_value = speed_value - DELTA_SPEED
        left_speed.ChangeDutyCycle(speed_value)
        right_speed.ChangeDutyCycle(speed_value)
    #print(f"Current speed is {speed}.")


