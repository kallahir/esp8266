from led.pwmled import PwmLed
import time

class RgbLed:
    def __init__(self, r, g, b):
        self.__red = PwmLed(r, freq=1000)
        self.__green = PwmLed(g, freq=1000)
        self.__blue = PwmLed(b, freq=1000)

    def red(self):
        self.color(255,0,0)

    def green(self):
        self.color(0,255,0)
    
    def blue(self):
        self.color(0,0,255)
    
    def white(self):
        self.color(255,255,255)

    def off(self):
        self.color(0,0,0)
    
    def cycle(self, times):
        for _ in range(times):
            self.red()
            time.sleep(0.1)
            self.green()
            time.sleep(0.1)
            self.blue()
            time.sleep(0.1)
        self.off()
    
    def cops(self, times):
        for _ in range(times):
            self.red()
            time.sleep(0.1)
            self.white()
            time.sleep(0.005)
            self.blue()
            time.sleep(0.1)
        self.off()

    def color(self, r, g, b):
        rv, gv, bv = RgbLed.__convert_rgb_to_pwm(r), RgbLed.__convert_rgb_to_pwm(g), RgbLed.__convert_rgb_to_pwm(b)
        self.__red.duty_u16(rv)
        self.__green.duty_u16(gv)
        self.__blue.duty_u16(bv)
    
    def __convert_rgb_to_pwm(value):
        return ((value * 257)-65536) * -1