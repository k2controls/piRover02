''' Uses message service to capture smartphone messages.
    Continues until LED OFF message received.
    11/30/23'''
from MessageService import MessageService

def do_test():
    print("Test Message Service - a smartphone connect is required!")
    print("Press LED OFF button to exit. (two presses required)")
    ms = MessageService()
    message = ""
    while message != "0,0,0,0,0,0,8,0,0": #LED OFF button 
        message = ms.get_message()
        print(message)
    print()

if __name__ == "__main__":
    do_test()