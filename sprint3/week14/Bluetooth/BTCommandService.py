''' Bluetooth Comand Service
Captures serial bluetooth message and 
decodes to a rover command.
12/6/2022
'''
from serial import Serial
from BTCommands import CommandType, CommandID, Messages

class Command():

    def __init__(self, 
            command_type:CommandType, 
            command_id:CommandID=None, 
            value:int=None, 
            message:str=None):
        self.command_type = command_type
        self.command_id = command_id
        self.value = value
        self.message = message

    def __str__(self):
        s = f"{self.message}\n{self.command_type}\t{self.command_id}\t{self.value}"
        return s

class BTCommandService:

    def __init__(self) -> None:
        self.serial_port =Serial("/dev/ttyAMA0", 9600)
        self.command_list = []

    def _get_message(self) -> str:
        '''Return message string from smartphone app.'''
        #wait for start
        input_str = ""
        while self.serial_port.read(1).decode() != "$":
            pass
        #wait for end
        while True:
            char = self.serial_port.read(1).decode()
            if char == "#":
                break
            input_str += char
        return input_str

    def _get_analog_value(self, message:str) -> int:
        ''' Extracts value from analog message'''
        return_val = None
        while message[0].isalpha():
            message = message[1:]
        if message.isdigit():
            return_val = int(message)
        return return_val   

    def _decode_message(self, message):
        command = None
        parts = message.split(",")
        if parts[0] == "4WD":
            key = parts[1][:3]
            if key == "PTZ":
                command = Command(
                    command_type=CommandType.ANALOG,
                    command_id=CommandID.SERVO_ANALOG,
                    message=parts[1])
                command.value = self._get_analog_value(parts[1])
            elif key == "CLR":
                self._decode_leds_message(message)
                command = self.command_list.pop()
            elif key == "MOD":
                command = Command(
                    command_type=CommandType.MODE,
                    message = parts[1])
                command.command_type = Messages.MODE_MESSAGES[parts[1]]
        elif message in Messages.BUTTON_MESSAGES.keys():
            command= Command(
                command_type=CommandType.CONTROL,
                message=message)
            command.command_id = Messages.BUTTON_MESSAGES[message]
        return command

    def _decode_leds_message(self, message:str):
        ''' Creates individual LED messages from multipart slider message.'''
        message_list = message.split(",")
        self._decode_led_message(CommandID.LED_RED_ANALOG, message_list[1])
        self._decode_led_message(CommandID.LED_GREEN_ANALOG, message_list[2])
        self._decode_led_message(CommandID.LED_BLUE_ANALOG, message_list[3])
        
        
    def _decode_led_message(self, command_id:CommandID, led_message:str):
        ''' Create LED analog commands from led message'''
        command = Command(
            command_type=CommandType.ANALOG,
            command_id=command_id,
            message=led_message)
        command.value = self._get_analog_value(led_message)
        self.command_list.append(command)
        
    def get_command(self) -> Command:
        ''' Gets command from queue or waits for next.'''
        if self.command_list: #prior LED command waiting?
            command = self.command_list.pop()
        else:
            message = self._get_message()
            command = self._decode_message(message)
        return command


