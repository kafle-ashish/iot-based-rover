from packages import control_fetch 
from packages.gpio_control import GPIOControl 
#from packages.mjpg_streamer import streamer
#import sensors
import threading
import os

def onStartUP():
    os.system("sudo modprobe bcm2835-v4l2")
    #streamer.stream()
    #pass

def looper():

    clock = 0
    while(True):
        #print("Getting data......")
        DATA = str(control_fetch.get_data())
        print(DATA)
        if DATA == "['0000']":
            th = threading.thread(target=gpio_control.wait())
            #gpio_control.wait()

        elif DATA == "['0001']":            
            th = threading.thread(target=gpio_control.left()) 
            #gpio_control.left()

        elif DATA == "['0002']":
            th = threading.thread(target=gpio_control.forward())
            #gpio_control.forward()
        
        elif DATA == "['0003']":
            th = threading.thread(target=gpio_control.right())
            #gpio_control.right()
        
        elif DATA == "['0004']":
            th = threading.thread(target=gpio_control.reverse())
            #gpio_control.reverse()
        
        else:
            pass
            #gpio_control.wait()

        #clock += 1
        #if clock == 100:
            #sensors.post()
            #clock = 0
    #return

if __name__ == "__main__":
   # onStartUP()
    gpio_control = GPIOControl()
    looper()
