#!/usr/bin/python
from fc_lib import *
import signal
import os
import opc
import sys
import time

pid = str(os.getpid())
pidfile = "/var/run/strobe.pid"

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
    
numLEDs = 800
black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs

while True:
    client.put_pixels(white)
    time.sleep(0.05) 
    client.put_pixels(black)
    time.sleep(0.05)
