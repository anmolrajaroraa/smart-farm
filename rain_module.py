from gpiozero import InputDevice
from time import sleep


no_rain=InputDevice(16)
def rain():
    if not no_rain.is_active:
        #print("Its raining")
        return ("1")
    else:
        #print("no rain")
        return ("0")
    

    