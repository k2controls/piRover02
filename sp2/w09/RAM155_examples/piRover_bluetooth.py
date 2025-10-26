''' piRover Bluetooth module
Provides interface to Yahboom smartphone
app enabling remote control of the piRover.
Keith E. Kelly
v 2.1 - added LED_OFF
11/30/23
'''
from serial import Serial

MESSAGES = {
        "0,0,0,0,0,0,0,0,0":    "STOP"
        ,"1,0,0,0,0,0,0,0,0":   "FORWARD"
        ,"2,0,0,0,0,0,0,0,0":   "BACKWARD"
        ,"3,0,0,0,0,0,0,0,0":   "LEFT"
        ,"4,0,0,0,0,0,0,0,0":   "RIGHT"
        ,"0,1,0,0,0,0,0,0,0":   "LEFT_ALT"
        ,"0,2,0,0,0,0,0,0,0":   "RIGHT_ALT"
        ,"0,0,1,0,0,0,0,0,0":   "BEEP"
        ,"0,0,0,1,0,0,0,0,0":   "SPEED_UP"
        ,"0,0,0,2,0,0,0,0,0":   "SPEED_DOWN"
        ,"0,0,0,0,1,0,0,0,0":   "SERVO_LEFT"
        ,"0,0,0,0,2,0,0,0,0":   "SERVO_RIGHT"
        ,"0,0,0,0,0,0,1,0,0":   "LED_ON"
        ,"0,0,0,0,0,0,2,0,0":   "LED_RED"
        ,"0,0,0,0,0,0,3,0,0":   "LED_GREEN"
        ,"0,0,0,0,0,0,4,0,0":   "LED_BLUE"
        ,"0,0,0,0,0,0,8,0,0":   "LED_OFF"
        ,"0,0,0,0,0,0,0,0,1":   "SERVO_MID"
        # ,"0,0,0,0,0,0,0,1,0":   "OUTFIRE"
        # servo analog example "4WD,PTZ90"
        ,"4WD,PTZ"          :    "SERVO_ANALOG"
        # led analog example "4WD,CLR255,CLG0,CLB0"
        ,"4WD,CLR"          :    "LED_ANALOG"
        }

serial_port = None
command_list = []

def bluetooth_init():
    global serial_port
    serial_port = Serial("/dev/ttyAMA0", 9600)
            
def _get_message() -> str:
    #wait for start
    input_str = ""
    while serial_port.read(1).decode() != "$":
        pass
    #wait for end
    while True:
        char = serial_port.read(1).decode()
        if char == "#":
            break
        input_str += char
    return input_str

def _get_analog_value(message:str) -> int:
    return_val = None
    while message[0].isalpha():
        message = message[1:]
    if message.isdigit():
        return_val = int(message)
    return return_val   

def _decode_led_message(message:str):
    message_list = message.split(",")
    led_message = message_list[1]
    command_id = "RED_LED_ANALOG"
    command_value = _get_analog_value(led_message)
    command_list.append([command_id,command_value])
    led_message = message_list[2]
    command_id = "GREEN_LED_ANALOG"
    command_value = _get_analog_value(led_message)
    command_list.append([command_id,command_value])
    led_message = message_list[3]
    command_id = "BLUE_LED_ANALOG"
    command_value = _get_analog_value(led_message)
    command_list.append([command_id,command_value])

def get_command() -> tuple:
    if command_list:
        next_command = command_list.pop()
        command_id = next_command[0]
        command_value = next_command[1]
    else:
        message = _get_message()
        print(message)

        if message[0:7] == "4WD,PTZ":
            command_id = "SERVO_ANALOG"
            command_value = int(message[7:])
        elif message[0:7] == "4WD,CLR":
            _decode_led_message(message)   
            next_command = command_list.pop()
            command_id = next_command[0]
            command_value = next_command[1]
        elif message in MESSAGES.keys():
            command_id = MESSAGES[message]
            command_value = None
        else:
            print("ERROR: Message not supported.")
    return command_id, command_value

