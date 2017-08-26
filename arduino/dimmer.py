import binascii
from time import sleep
from Xlib import display
import serial
ser = serial.Serial('/dev/ttyACM0')

dpy = display.Display().screen().root
while ser.isOpen():
    data = dpy.query_pointer()._data
    x = data['root_x'] / 1920
    y = data['root_y'] / 1200
    bytes = (
        int(116).to_bytes(1, byteorder='big') +
        int(100 * x).to_bytes(1, byteorder='big') +
        int(100 * (1 - y)).to_bytes(1, byteorder='big')
    )
    print(binascii.hexlify(bytes))
    ser.write(bytes)

ser.close()
