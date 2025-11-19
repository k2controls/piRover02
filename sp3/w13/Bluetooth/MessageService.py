''' Message Service
Fetches Rover message for remote device using
Bluetooth serial connection
V2.1
11/30/23
'''
from serial import Serial

class MessageService():

    def __init__(self):
        self.serial = Serial("/dev/ttyAMA0", 9600)
            
    def get_message(self) -> str:
        #wait for start
        input_str = ""
        while self.serial.read(1).decode() != "$":
            pass
        #wait for end
        while True:
            char = self.serial.read(1).decode()
            if char == "#":
                break
            input_str += char
        return input_str

