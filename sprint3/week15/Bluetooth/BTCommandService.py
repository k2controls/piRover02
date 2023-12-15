''' Bluetooth Comand Service
Captures serial bluetooth message and 
decodes to a rover command.
V2.1
V2.2 - check for missing stop char
v3.0 - testing required
12/7/23
'''
TEST = True

if not TEST:
    from serial import Serial
from BTCommands import CommandType, CommandID, Messages

class Command():
    # Data object that contains command parameters
    def __init__(self, 
            command_type:CommandType=None, 
            command_id:CommandID=None, 
            value:int=None, 
            message:str=None):
        self.command_type = command_type
        self.command_id = command_id
        self.value = value
        self.message = message

    def __str__(self):
        # Enables print(command)
        s = f"{self.message}\n{self.command_type}\t{self.command_id}\t{self.value}"
        return s

class BTCommandService:
    # Service to capture and parse command
    def __init__(self) -> None:
        if not TEST:
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
            if char == "#" or char == "$":  #v2.2 added check for missing stop
                 break
            input_str += char
        return input_str
    
    def _load_commands(self, message:str):
        '''Loads command objects based on message string.'''
        segs = message.split(",")
        if segs[0] == "4WD":
            if segs[1][0:3] == "PTZ":
                cmd = Command(CommandType.ANALOG, CommandID.SERVO_ANALOG, message=segs[1])
                self._set_command_value(cmd)
                self.command_list.append(cmd)
            elif segs[1][:4] == "MODE":
                cmd = Command(CommandType.MODE, message=segs[1])
                self._set_command_id(cmd)
                self.command_list.append(cmd)
            elif segs[1][:2] == "CL":
                cmd = Command(CommandType.ANALOG, message=segs[1])
                self._set_command_id(cmd)
                self._set_command_value(cmd)
                self.command_list.append(cmd)
                cmd = Command(CommandType.ANALOG, message=segs[2])
                self._set_command_id(cmd)
                self._set_command_value(cmd)
                self.command_list.append(cmd)
                cmd = Command(CommandType.ANALOG, message=segs[3])
                self._set_command_id(cmd)
                self._set_command_value(cmd)
                self.command_list.append(cmd)
        else:
            cmd = Command(CommandType.CONTROL, message=message)
            self._set_command_id(cmd)
            self.command_list.append(cmd)  

    def _set_command_id(self, command:Command):
        '''Set command_id base on type and message.'''
        if command.command_type == CommandType.CONTROL:
            command.command_id = Messages.BUTTON_MESSAGES[command.message]
        elif command.command_type == CommandType.MODE:
            command.command_id = Messages.MODE_MESSAGES[command.message]
        elif command.command_type == CommandType.ANALOG and command.message[0:3] == "PTZ":
            command.command_id = CommandID.SERVO_ANALOG
        elif command.command_type == CommandType.ANALOG and command.message[0:3] == "CLR":
            command.command_id = CommandID.LED_RED_ANALOG
        elif command.command_type == CommandType.ANALOG and command.message[0:3] == "CLG":
            command.command_id = CommandID.LED_GREEN_ANALOG    
        elif command.command_type == CommandType.ANALOG and command.message[0:3] == "CLB":
            command.command_id = CommandID.LED_BLUE_ANALOG

    def _set_command_value(self, command:Command):
        '''Set value for analog command messages.'''
        m =  command.message
        while m[0].isalpha():
            m = m[1:]
        if m.isdigit():
            command.value = int(m)

    def get_command(self) -> Command:
        ''' Gets command from queue or waits for next.'''
        if self.command_list: #prior LED command waiting?
            command = self.command_list.pop()
        else:                   # wait for next
            message = self._get_message()
            self._load_commands(message)
            command = self.command_list.pop()
        return command

