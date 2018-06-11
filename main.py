from packages import control_fetch 
from packages.gpio_control import GPIOControl
from packages.mjpg_streamer import streamer 
#import sensors
import threading
import os

def onStartUP():
    os.system("sudo modprobe bcm2835-v4l2")
    live_feed = threading.Thread(streamer.stream(), daemon=True)
    return

def looper():

    clock = 0
    while(True):
        #print("Getting data......")
        DATA = str(control_fetch.get_data())
        print(DATA)
        if DATA == "['0000']":
            th = threading.Thread(target=gpio_control.wait(), daemon=True)
            #gpio_control.wait()
            pass

        elif DATA == "['0001']":            
            th = threading.Thread(target=gpio_control.left(), daemon=True) 
            #gpio_control.left()

        elif DATA == "['0002']":
            th = threading.Thread(target=gpio_control.forward(), daemon=True)
            #gpio_control.forward()
        
        elif DATA == "['0003']":
            th = threading.Thread(target=gpio_control.right(), daemon=True)
            #gpio_control.right()
        
        elif DATA == "['0004']":
            th = threading.Thread(target=gpio_control.reverse(), daemon=True)
            #gpio_control.reverse()
        
        elif DATA == "['0005']":
            break
        else:
            pass

        #clock += 1
        #if clock == 10:
            #th = threading.Thread(sensors.post(), daemon=True)
            #clock = 0

if __name__ == "__main__":
    onStartUP()
    gpio_control = GPIOControl()
    looper()
