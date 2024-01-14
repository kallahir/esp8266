from led.rgbled import RgbLed
from utils.pin import PinNum
import time

rgb_led = RgbLed(PinNum.D3, PinNum.D2, PinNum.D1)
rgb_led.cops(5)
rgb_led.color(255,0,255)
time.sleep(1)
rgb_led.off()