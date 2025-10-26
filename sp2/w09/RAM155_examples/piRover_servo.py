'''Module  to control piRover front servo'''
import RPi.GPIO as GPIO

SERVO_PIN = 16
DC_LEFT = 11.5
DC_RIGHT = 4
DC_CENTER = (DC_LEFT + DC_RIGHT)/2
DC_RANGE = DC_LEFT-DC_RIGHT

pwm_servo = None

def servo_init():
    global pwm_servo

    print("the servo is initialized.")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(SERVO_PIN, GPIO.OUT)
    pwm_servo = GPIO.PWM(SERVO_PIN, 50)
    pwm_servo.start(DC_CENTER)

def servo_left():
    print("The servo is rotated left.")
    pwm_servo.ChangeDutyCycle(DC_LEFT)

def servo_right():
    print("The servo is rotated right.")
    pwm_servo.ChangeDutyCycle(DC_RIGHT)

def servo_center():
    print("the servo is centered.")
    pwm_servo.ChangeDutyCycle(DC_CENTER)

def servo_set_position(new_position):
    if new_position >= 0 and new_position <= 180:
        print(f"Servo position is set to {new_position}.")
        set_point = DC_RANGE * new_position/180
        # dc = DC_RIGHT + set_point
        dc = DC_LEFT - set_point
        pwm_servo.ChangeDutyCycle(dc)
    else:
        print("Invalid position.")