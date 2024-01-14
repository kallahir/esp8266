from machine import Pin, PWM
import time

PWM_MIN=65536
PWM_MAX=0

class PwmLed:
    def __init__(self, pin_num, freq=500, duty=1024):
        self.__led_pin = Pin(pin_num, Pin.OUT)
        self.__led = PWM(self.__led_pin)
        self.__led.freq(freq)
        self.__led.duty(duty)
    
    def on(self):
        self.__led.duty_u16(PWM_MAX)
        time.sleep(0.005)

    def off(self):
        self.__led.duty_u16(PWM_MIN)
        time.sleep(0.005)

    def duty(self, value):
        self.__led.duty(value)

    def duty_u16(self, value):
        self.__led.duty_u16(value)
