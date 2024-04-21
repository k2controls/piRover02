''' Uses command service to capture smartphone messages and create resulting command objects.
    Continues until LED OFF message received.
    11/30/23'''
import sys
sys.path.append("/home/pi/RAM205/week14_bt_demo/Bluetooth")

from Bluetooth.BTCommandService import BTCommandService, Command, CommandID

def do_test():
    print("Test Command Service - a smartphone connect is required!")
    print("Press LED OFF button to exit. (two presses required)")
    bt_command_service = BTCommandService()
    
    while True:
        command = bt_command_service.get_command() 
        print(command)
        if command.command_id == CommandID.LED_OFF:
            break

if __name__ == "__main__":
    do_test()