from fc_lib import *
import os
import opc
import time
import signal
import sys

pid = str(os.getpid())
pidfile = "/var/run/mariovideo.pid"

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
    cap = cv2.VideoCapture('/home/pi/fadecandy_shenanigans/mario.mkv')
    while True:
            ret, img = cap.read()
            #print s
            #cv2.imshow('test',img)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
            #array = opencv_image_to_array(img) 
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(rgb, (32, 25)).tolist()
            flat =  [item for sublist in resized for item in sublist]
            array = fix_array(flat)
            ##client.put_pixels([[0,0,0]]*800)
            client.put_pixels(array)
            #client.put_pixels(array)
            time.sleep(1/60.)
    cap.release()
    cv2.destroyAllWindows()
