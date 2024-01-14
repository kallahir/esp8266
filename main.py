from led.rgbled import RgbLed
from utils.pin import PinNum
from sensors.hcsr04 import HCSR04 
import time

rgb_led = RgbLed(PinNum.D3, PinNum.D2, PinNum.D1)
distance_sensor = HCSR04(PinNum.D6, PinNum.D5)

while True:
    d = distance_sensor.distance_cm()
    if d < 15.0:
        rgb_led.cops(2)
    elif d > 15.0:
        rgb_led.green()
    time.sleep(0.3)
