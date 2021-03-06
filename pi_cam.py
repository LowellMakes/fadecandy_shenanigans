#!/usr/bin/python
from fc_lib import *
import opc
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import os
import sys
import signal

pid = str(os.getpid())
pidfile = "/var/run/fadecandy.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()
else:
    file(pidfile, 'w').write(pid)

def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)
def on_exit(sig, func=None):
    print "exit handler triggered"
    sys.exit(1)

if __name__ == '__main__':
    set_exit_handler(on_exit)
    client = opc.Client('localhost:7890')
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,480))
    time.sleep(0.1)
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            img = frame.array
            img = cv2.flip(img,1)
            array = opencv_image_to_array(img) 
            client.put_pixels(array)
            client.put_pixels(array)
            rawCapture.truncate(0)
