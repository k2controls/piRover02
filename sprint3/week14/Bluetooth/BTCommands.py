''' Contains data definitions for Bluetooth messaging
Keith E. Kelly
v 2.1 - Added LED_OFF,LED_ON
11/30/23
'''
from enum import Enum

class CommandType(Enum):
    CONTROL     = 0
    ANALOG      = 1
    MODE        = 2

class CommandID(Enum):
    STOP                = 0
    FORWARD             = 1
    BACKWARD            = 2
    LEFT                = 4
    RIGHT               = 5
    LEFT_ALT            = 6
    RIGHT_ALT           = 7
    BEEP                = 8
    SPEED_UP            = 9
    SPEED_DOWN          = 10
    SERVO_LEFT          = 11
    SERVO_RIGHT         = 12
    LED_OFF             = 13
    LED_ON              = 14
    LED_RED             = 15
    LED_GREEN           = 16
    LED_BLUE            = 17
    SERVO_MID           = 18
    OUTFIRE             = 19    # this is in the docs. Not sure what it is.
    
    GIMBAL_UP           = 20
    GIMBAL_DOWN         = 21
    GIMBAL_RIGHT        = 22
    GIMBAL_LEFT         = 23
    GIMBAL_BTN_RELEASE  = 24
    #ANALOG MESSAGES
    SERVO_ANALOG        = 100     #REQUIRES VALUE 
    LED_RED_ANALOG      = 101     #REQUIRES VALUE 
    LED_GREEN_ANALOG    = 102     #REQUIRES VALUE 
    LED_BLUE_ANALOG     = 103     #REQUIRES VALUE 
    #MODE MESSAGES
    COLORFUL_STOP       = 200
    COLORFUL_START      = 201
    TRACKING_STOP       = 202
    TRACKING_START      = 203
    OBSTACLE_START      = 204
    OBSTACLE_STOP       = 205

class Messages():

    MODE_MESSAGES = {
        "MODE20":   CommandID.TRACKING_STOP,
        "MODE21":   CommandID.TRACKING_START,
        "MODE30":   CommandID.OBSTACLE_STOP,
        "MODE31":   CommandID.OBSTACLE_START,
        "MODE40":	CommandID.COLORFUL_STOP,
        "MODE41":	CommandID.COLORFUL_START
        }

    ANALOG_MESSAGES = {
        "PTZ":  CommandID.SERVO_ANALOG,
        "CLR":  CommandID.LED_RED_ANALOG,
        "CLG":  CommandID.LED_GREEN_ANALOG,
        "CLB":  CommandID.LED_BLUE_ANALOG
    }
        
    BUTTON_MESSAGES = {
        "0,0,0,0,0,0,0,0,0": CommandID.STOP
        ,"1,0,0,0,0,0,0,0,0": CommandID.FORWARD
        ,"2,0,0,0,0,0,0,0,0": CommandID.BACKWARD
        ,"3,0,0,0,0,0,0,0,0": CommandID.LEFT
        ,"4,0,0,0,0,0,0,0,0": CommandID.RIGHT
        ,"0,1,0,0,0,0,0,0,0": CommandID.LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0": CommandID.RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0": CommandID.BEEP
        ,"0,0,0,1,0,0,0,0,0": CommandID.SPEED_UP
        ,"0,0,0,2,0,0,0,0,0": CommandID.SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0": CommandID.SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0": CommandID.SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0": CommandID.LED_ON
        ,"0,0,0,0,0,0,2,0,0": CommandID.LED_RED
        ,"0,0,0,0,0,0,3,0,0": CommandID.LED_GREEN
        ,"0,0,0,0,0,0,4,0,0": CommandID.LED_BLUE
        ,"0,0,0,0,0,0,0,0,1": CommandID.SERVO_MID
        ,"0,0,0,0,0,0,0,1,0": CommandID.OUTFIRE
        ,"0,0,0,0,0,0,8,0,0": CommandID.LED_OFF
        ,"0,0,0,0,3,0,0,0,0": CommandID.GIMBAL_UP
        ,"0,0,0,0,4,0,0,0,0": CommandID.GIMBAL_DOWN
        ,"0,0,0,0,7,0,0,0,0": CommandID.GIMBAL_RIGHT
        ,"0,0,0,0,6,0,0,0,0": CommandID.GIMBAL_LEFT 
        ,"0,0,0,0,8,0,0,0,0": CommandID.GIMBAL_BTN_RELEASE
    }

