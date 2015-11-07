#!/usr/bin/python
from fc_lib import *
import opc
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import os
import sys
import signal

pid = str(os.getpid())
pidfile = "/var/run/fc_loop.pid"
# Set Gpio pin to pin14, first pin next to GND. It's also TX, hopefuly that's not a problem.
gpioPin = 14
start = time.time()


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

def check_button():
    global start
    global mode
    btn = not GPIO.input(gpioPin)
    if btn:
        time.sleep(0.5)
        start = time.time()
        if mode == "animation":
            mode = "video"
        else:
            mode = "animation"
    return btn

if __name__ == '__main__':
    set_exit_handler(on_exit)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    mode = "animation"
    client = opc.Client('localhost:7890')
    mario_paths = ['/home/pi/fadecandy_shenanigans/mario_images/mario2.jpg',
             '/home/pi/fadecandy_shenanigans/mario_images/mario3.jpg',
             '/home/pi/fadecandy_shenanigans/mario_images/mario1.jpg']
    images = [read_image_to_array(path) for path in mario_paths]
    marios = images
    paths = ['/home/pi/fadecandy_shenanigans/pacman_images/pacman_0_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_1_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_2_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_3_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_4_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_5_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_6_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_7_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_8_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_9_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_10_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_11_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_12_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_13_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_14_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_15_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_16_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_17_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_18_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_19_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_20_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_21_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_22_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_23_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_24_resize.jpg',
	'/home/pi/fadecandy_shenanigans/pacman_images/pacman_25_resize.jpg']
    images = [opencv_image_to_array(cv2.imread(path)) for path in paths]
    pacmans = images
    paths = ['/home/pi/fadecandy_shenanigans/fourth_images/lmsv005-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv010-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv015-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv020-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv025-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv030-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv035-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv040-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv045-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv050-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv055-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv060-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv065-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv070-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv075-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv080-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv085-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv090-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv095-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv100-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv105-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv110-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv115-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv120-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv125-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv130-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv135-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv140-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv145-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv150-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv155-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv160-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv165-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv170-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv175-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv180-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv185-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv190-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv195-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv200-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv205-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv210-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv215-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv220-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv225-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv230-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv235-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv240-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv245-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv525-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv530-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv535-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv540-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv545-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv550-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv550-invert.jpg',
             '/home/pi/fadecandy_shenanigans/fourth_images/lmsv550-invert.jpg']
    images = [opencv_image_to_array(cv2.imread(path)) for path in paths]
    texts = images
    
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,480))
    time.sleep(0.1)

#    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#            img = frame.array
#            img = cv2.flip(img,1)
#            array = opencv_image_to_array(img) 
#            client.put_pixels(array)
#            client.put_pixels(array)
#            rawCapture.truncate(0)
    start = time.time()
    while True:
        if mode == "animation":
            seconds = time.time()-start
            if seconds<10:
                for image in marios:
                    client.put_pixels(image)
                    client.put_pixels(image)
                    if check_button():
                        break;
                    time.sleep(0.11)
            elif seconds<20:
                for image in pacmans:
                    client.put_pixels(image)
                    if check_button():
                        break;
            elif seconds<30:
                for image in texts:
                    client.put_pixels(image)
                    if check_button():
                        break;
                    time.sleep(0.15)
            else:
                start = time.time()
        else:
            for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                img = frame.array
                img = cv2.flip(img,1)
                array = opencv_image_to_array(img)
                client.put_pixels(array)
                client.put_pixels(array)
                rawCapture.truncate(0)
                if check_button():
                    break

