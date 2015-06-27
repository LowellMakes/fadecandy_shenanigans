from fc_lib import *
import opc
import time
import cv2

if __name__ == '__main__':
    client = opc.Client('localhost:7890')
    
    paths = ['smiley1.jpg',
             'smiley2.jpg',
             'smiley3.jpg',
             'smiley4.jpg']
    images = [opencv_image_to_array(cv2.imread(path)) for path in paths]
    images = images + images[::-1]
    while True:
        for image in images:
            client.put_pixels(image)
            client.put_pixels(image)
            time.sleep(0.25)
