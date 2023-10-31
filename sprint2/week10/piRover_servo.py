''' Module to control piRover servo
(front servo)
'''
import RPi.GPIO as GPIO

SERVO_PIN = 16
DC_LEFT = 11
DC_RIGHT = 2
DC_CENTER = (DC_LEFT + DC_RIGHT)/2
DC_RANGE = DC_LEFT - DC_RIGHT

pwm_servo = None
servo_dc = None

def servo_init():
    global pwm_servo
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(SERVO_PIN, GPIO.OUT)
    pwm_servo = GPIO.PWM(SERVO_PIN, 50)
    servo_dc = DC_CENTER
    pwm_servo.start(servo_dc)
    print("Servo is initialized")

def servo_left(): #ccw
    pwm_servo.ChangeDutyCycle(DC_LEFT)
    print("Servo is rotated to the left")

def servo_right():  #cw
    pwm_servo.ChangeDutyCycle(DC_RIGHT)
    print("Servo is rotated to the right")

def servo_center():
    pwm_servo.ChangeDutyCycle(DC_CENTER)
    print("Servo is centered.")

def servo_set_position(new_position):
    if new_position >= 0 and new_position <= 180:
        print(f"Servo position is set to {new_position}.")
        set_point = DC_RANGE * new_position/180
        dc = DC_LEFT - set_point
        pwm_servo.ChangeDutyCycle(dc)
    else:
        print("Invalid position")