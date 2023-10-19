''' piRover Bluetooth module
Provides interface to Yahboom smartphone
app enabling remote control of the piRover.
See next_action use in sample code at the bottom 
of this module.

Keith E. Kelly
11/16/20
'''
import time
from serial import Serial
from threading import Thread
from enum import Enum
from queue import SimpleQueue

class Action(Enum):
    STOP            = 0
    FORWARD         = 1
    BACKWARD        = 2
    LEFT            = 3
    RIGHT           = 4
    LEFT_ALT        = 5
    RIGHT_ALT       = 6

    BEEP            = 8
    SPEED_UP        = 9
    SPEED_DOWN      = 10
    SERVO_LEFT      = 11
    SERVO_MID       = 12
    SERVO_RIGHT     = 13
    LED_OFF         = 14
    LED_RED         = 15
    LED_GREEN       = 16
    LED_BLUE        = 18
    OUTFIRE         = 19

class ActionKey(object):
    def __init__(self, action: Action):
        self.action = action
        self.time_stamp = time.time()

    def is_old(self):
        return self.time_stamp < time.time() - 1

    def __str__(self):
        return f"{self.action.name} occurred at {self.time_stamp}."


class Bluetooth(Thread):

    Messages = {
         "0,0,0,0,0,0,0,0,0": Action.STOP
        ,"1,0,0,0,0,0,0,0,0": Action.FORWARD
        ,"2,0,0,0,0,0,0,0,0": Action.BACKWARD
        ,"3,0,0,0,0,0,0,0,0": Action.LEFT
        ,"4,0,0,0,0,0,0,0,0": Action.RIGHT
        ,"0,1,0,0,0,0,0,0,0": Action.LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0": Action.RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0": Action.BEEP
        ,"0,0,0,1,0,0,0,0,0": Action.SPEED_UP
        ,"0,0,0,2,0,0,0,0,0": Action.SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0": Action.SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0": Action.SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0": Action.LED_OFF
        ,"0,0,0,0,0,0,2,0,0": Action.LED_RED
        ,"0,0,0,0,0,0,3,0,0": Action.LED_GREEN
        ,"0,0,0,0,0,0,4,0,0": Action.LED_BLUE
        ,"0,0,0,0,0,0,0,0,1": Action.SERVO_MID
        ,"0,0,0,0,0,0,0,1,0": Action.OUTFIRE
        ,"0,0,0,0,0,0,8,0,0": Action.LED_OFF
    }
  
    def __init__(self):
        self.serial = Serial("/dev/ttyAMA0", 9600)
        Thread.__init__(self)
        self.event_queue = SimpleQueue()
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            command_string = self._get_command_string()
            action = Bluetooth.Messages[command_string]
            action_key = ActionKey(action)
            self.event_queue.put(action_key)    
            
    def _get_command_string(self):
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

    def next_action(self):
        action_key = None
        while action_key == None:
            if not self.event_queue.empty():
                next = self.event_queue.get(block=False)
                if not next.is_old():
                    action_key = next
        return action_key.action

   
    # def isOpen(self):
    #     return self.serial.is_open()




if __name__ == "__main__":
    bt = Bluetooth()
    while(True):
        time.sleep(.1)
        action = bt.next_action()
        print(action.name)

