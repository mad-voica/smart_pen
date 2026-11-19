"""
This is a special demo that takes input over serial (not BLE) and shows that the pen 
can transmit data and write on a writing surface. 

Serial Input Taken:
    x, y, z, gx, gy, gz, magx, magy, magz

Somehow turn that into handwriting, probably on OpenCV display

@author Rishaan Bansal
"""

import pyserial
import cv2
import numpy as np

timelast = 0

def main():
    pass
    # initialize at the start of main - set position to 0
    # get accelerometer data over time, integrate twice at sampling rate to get position



if name == "__main__":
    main()

