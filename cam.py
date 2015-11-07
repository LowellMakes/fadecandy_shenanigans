#!/usr/bin/python
from fc_lib import *
import opc
import time

if __name__ == '__main__':
    client = opc.Client('localhost:7890')
    cam = cv2.VideoCapture(0)
    while True:
            s, img = cam.read()
            img = cv2.flip(img,1)
            array = opencv_image_to_array(img) 
            client.put_pixels(array)
            client.put_pixels(array)
            time.sleep(1/60.)
