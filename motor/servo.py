from machine import Pin, PWM

class Servo:
    def __init__(self, pin_num):
        self.__servo = PWM(Pin(pin_num, Pin.OUT))
        self.__servo.freq(50)
        self.__servo.duty(0)

    def open(self):
        self.angle(0)
    
    def close(self):
        self.angle(180)

    def angle(self, value):
        self.__servo.duty(Servo.map(value,0,180,20,125))

    def map(x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)