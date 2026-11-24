"""
This is a special demo that takes input over serial (not BLE) and shows that the pen 
can transmit data and write on a writing surface. 

Serial Input Taken:
    x, y, z, gx, gy, gz, magx, magy, magz

Somehow turn that into handwriting, probably on OpenCV display

@author Rishaan Bansal
"""

import serial
import cv2
import numpy as np
from datetime import datetime

timelast = datetime.now()
timedelta = datetime.now()
x = 0; # 0
y = 0; # 1
z = 0; # 2
gx = 0; # 3
gy = 0; # 4
gz = 0; # 5
magx = 0; # 6
magy = 0; # 7
magz = 0; # 8

ser = serial.Serial('/dev/cu.usbmodem1101', 112500, timeout=1)

image = np.zeros((512, 512, 3), dtype=np.uint8)

start = np.array([100, 100])

color = (0, 255, 0)
thickness = 2


def read_line():
    line = ser.readline()
    if line:
        text = line.decode('utf-8').strip()
        print(text)
        values = [float(a) for a in text.split(',')]
        return values
    return None

def main():
    while True:
        values = read_line()
        timedelta = datetime.now() - timelast
        timelast = datetime.now()
        print(f'Loop took: {timedelta}')


        x_delta = timelast * x # do a riemman sum
        y_delta = timelast * y

        new = np.array([(start[0] - x_delta), (start[1] - y_delta)])

        cv2.line(image, start, new, color, thickness) # draw a line from the current point according to x and y

        cv2.imshow('Line', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




    # get accelerometer data over time, integrate twice at sampling rate to get position



main()
