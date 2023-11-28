import time
import sys
sys.path.append("/home/pi/RAM205/weekFinal/model")

from BTCommandService import BTCommandService

bt_service = BTCommandService()
while True:
    command = bt_service.get_command()
    print(command)