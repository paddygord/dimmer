import binascii
from time import sleep
from Xlib import display
import serial
ser = serial.Serial('/dev/ttyACM0')

dpy = display.Display().screen().root
while ser.isOpen():
    data = dpy.query_pointer()._data
    bytes = (
        int(100 * data["root_x"] / 1920).to_bytes(1, byteorder='big') +
        int(100 * data["root_y"] / 1200).to_bytes(1, byteorder='big') +
        int(127).to_bytes(1, byteorder='big')
    )
    ser.write(bytes)

ser.close()
