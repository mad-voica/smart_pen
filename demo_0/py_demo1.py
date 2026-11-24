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
magx = 13; # 6
magy = -33; # 7
magz = 0; # 8

ser = serial.Serial('/dev/cu.usbmodem1101', 112500, timeout=1)

image = np.zeros((512, 512, 3), dtype=np.uint8)

start = np.array([100, 100])

color = (0, 255, 0)
thickness = 2


SCALE = 10  # pixels per meter, tune this

def read_line():
    line = ser.readline()
    if not line:
        return None
    try:
        values = [float(v) for v in line.decode('utf-8', errors='ignore').strip().split(',')]
        return values if len(values) == 9 else None
    except ValueError:
        return None

def main():
    pos = np.array([256.0, 256.0])   # pen position in pixels
    vel = np.zeros(2)                # m/s
    timelast = datetime.now()
    vals_last = [13, -33]

    while True:
        values = read_line()
        print(values)
        if values is None:
            continue

        now = datetime.now()
        dt = (now - timelast).total_seconds()
        timelast = now

        accel = np.array([values[6], values[7]]) - vals_last  # x, y
        vals_last = [values[6], values[7]]
        #vel += accel * dt                          # 1st integral
        new = pos + accel * SCALE               # 2nd integral

        cv2.line(image, tuple(pos.astype(int)), tuple(new.astype(int)), color, thickness)
        pos = new

        cv2.imshow('Line', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    # get accelerometer data over time, integrate twice at sampling rate to get position



main()
