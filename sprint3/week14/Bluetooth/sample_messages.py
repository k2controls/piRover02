''' Typical Bluetooth messages from smartphone.
    For discussion only. Not used.
    4/17/2024
'''
bluetooth_sample_messages = [
        "0,0,0,0,0,0,0,0,0"            #STOP
        ,"1,0,0,0,0,0,0,0,0"           #FORWARD
        ,"2,0,0,0,0,0,0,0,0"           #BACKWARD
        ,"3,0,0,0,0,0,0,0,0"           #LEFT
        ,"4,0,0,0,0,0,0,0,0"           #RIGHT
        ,"0,1,0,0,0,0,0,0,0"           #LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0"           #RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0"           #BEEP
        ,"0,0,0,1,0,0,0,0,0"           #SPEED_UP
        ,"0,0,0,2,0,0,0,0,0"           #SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0"           #SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0"           #SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0"           #LED_OFF
        ,"0,0,0,0,0,0,2,0,0"           #LED_RED
        ,"0,0,0,0,0,0,3,0,0"           #LED_GREEN
        ,"0,0,0,0,0,0,4,0,0"           #LED_BLUE
        ,"0,0,0,0,0,0,0,0,1"           #SERVO_MID
        ,"0,0,0,0,0,0,0,1,0"           #OUTFIRE
        ,"0,0,0,0,0,0,8,0,0"           #LED_OFF
        ,"0,0,0,0,3,0,0,0,0"           #GIMBAL_DOWN - GIMBAL_UP missing one
        ,"0,0,0,0,4,0,0,0,0"           #GIMBAL_RIGHT
        ,"0,0,0,0,7,0,0,0,0"           #GIMBAL_RIGHT
        ,"0,0,0,0,6,0,0,0,0"           #GIMBAL_LEFT
        ,"0,0,0,0,8,0,0,0,0"           #GIMBAL_BTN_release
        ,"4WD,PTZ180"                  #Servo with value of 180 rotation
        ,"4WD,PTZ90"                   #Servo with value of 90 rotation
        ,"4WD,PTZ0"                    #Servo with value of 0 rotation
        ,"4WD,CLR255,CLG255,CLB255"    #LED with RGB from 0 to 255 for each
        ,"4WD,MODE40"                  #Colorful stop
        ,"4WD,MODE41"                  #Colorful Start
        ,"4WD,MODE20"                  #Tracking Stop
        ,"4WD,MODE21"                  #Tracking Start 
        ,"4WD,MODE30"                  #Obstacle Stop
        ,"4WD,MODE31"                  #Obstacle Start
    ]