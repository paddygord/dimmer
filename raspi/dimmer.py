import RPi.GPIO as gpio
from time import sleep
from datetime import datetime
import math

gpio.setmode(gpio.BCM)

ch0 = 3
ch1 = 2
sync = 4
gpio.setup((ch0, ch1), gpio.OUT, initial=gpio.LOW)
gpio.setup(sync, gpio.IN)

try:
    while True:
        if gpio.wait_for_edge(sync, gpio.RISING, timeout=30) is None:
            print('timeout!')
            continue
        value0 = 0.5 + 0.5 * math.sin(datetime.now().timestamp())
        value0 *= 1
        value0 = 1 - value0
        value0 = min(max(value0, 0.1), 1)
        print(value0)
        sleep(0.01 * value0)
        gpio.output(ch0, gpio.HIGH)
        gpio.output(ch1, gpio.HIGH)
        sleep(0.00001)
        gpio.output(ch0, gpio.LOW)
        gpio.output(ch1, gpio.LOW)
finally:
    gpio.cleanup()
