''' Uses command service to capture smartphone messages and create resulting command objects.
    Continues until LED OFF message received.
    4/17/2024'''

from BTCommandService import BTCommandService, Command, CommandID

def do_test():
    print("Test Command Service - a smartphone connect is required!")
    print("Press LED OFF button to exit. (two presses required)")
    bt_command_service = BTCommandService()
    
    while True:
        command = bt_command_service.get_command() 
        # print(command)
        print(f"command type: {command.command_type}")
        print(f"command id: {command.command_id}")
        print(f"command message: {command.message}")
        print(f"command value: {command.value}")
        print()
        if command.command_id == CommandID.LED_OFF:
            break

if __name__ == "__main__":
    do_test()