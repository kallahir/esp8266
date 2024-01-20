from machine import Pin
from utils.pin import PinNum

class Led:
    def __init__(self, pin_num=PinNum.D4):
        self.__led_pin = Pin(pin_num, Pin.OUT)
    
    def on(self):
        self.__led_pin.off()

    def off(self):
        self.__led_pin.on()
