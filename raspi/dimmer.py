from time import sleep
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

ch0 = 3
ch1 = 2
sync = 4
gpio.setup((ch0, ch1), gpio.OUT, initial=gpio.LOW)
gpio.setup(sync, gpio.IN)


import struct
import mmap
f = open('ui_file', 'a+b')
mm = mmap.mmap(f.fileno(), 16)


import math
value0 = 1
value1 = 1

time = 0
phase0 = 0
phase1 = 0

try:
    while True:
        if gpio.wait_for_edge(sync, gpio.RISING, timeout=15) is not None:
            if value0 < value1:
                sleep(0.01 * value0)
                gpio.output(ch0, gpio.HIGH)
                sleep(0.00001)
                gpio.output(ch0, gpio.LOW)
                sleep(0.01 * (value1 - value0))
                gpio.output(ch1, gpio.HIGH)
                sleep(0.00001)
                gpio.output(ch1, gpio.LOW)
            else:
                sleep(0.01 * value1)
                gpio.output(ch1, gpio.HIGH)
                sleep(0.00001)
                gpio.output(ch1, gpio.LOW)
                sleep(0.01 * (value0 - value1))
                gpio.output(ch0, gpio.HIGH)
                sleep(0.00001)
                gpio.output(ch0, gpio.LOW)

            mm.seek(0)
            b, c, m, w = struct.unpack('ffff', mm)

            time = time + 0.02
            phase_offset = c * 0.5
            #hz0 = 5 + 20 * (0.5 + 0.5 * math.sin(2 * math.pi * (         0.0 + time / 60)))
            #hz1 = 5 + 20 * (0.5 + 0.5 * math.sin(2 * math.pi * (phase_offset + time / 60)))
            #phase0 = math.modf(phase0 + 0.02 / hz0)[0]
            #phase1 = math.modf(phase1 + 0.02 / hz1)[0]
            #waves0 =        0.5 + 0.5 * math.sin(2 * math.pi * (         0.0 + phase0))
            #waves1 =        0.5 + 0.5 * math.sin(2 * math.pi * (phase_offset + phase1))

            #value0 = (1 - waves0 * w) * b
            #value1 = (1 - waves1 * w) * b

            p = 3
            value0 = (p - abs(time % (2 * p) - p)) / p
            #value0 = 1 - math.modf(time / 3)[0]
            value0 *= b
            value1 = 1 - math.modf(phase_offset + time / 3)[0]
            value1 *= b

            value0 = 0.15 + 0.75 * min(max(1 - math.pow(value0, 2.5), 0), 1)
            value1 = 0.15 + 0.75 * min(max(1 - math.pow(value1, 2.5), 0), 1)
finally:
    gpio.cleanup()
