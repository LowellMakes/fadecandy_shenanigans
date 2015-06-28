from fc_lib import *
import opc
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

if __name__ == '__main__':
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
