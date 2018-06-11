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
if __name__ == "__main__":
    #onStartUP()
    gpio_control = GPIOControl()
    clock = 0
    while(True):
        #print("Getting data......")
        DATA = str(control_fetch.get_data())
        #print(DATA)
        if DATA == "['0000']":
            th = threading.Thread(target=gpio_control.wait, daemon=True)
            th.start()

        elif DATA == "['0001']":            
            th = threading.Thread(target=gpio_control.left, daemon=True) 
            th.start()

        elif DATA == "['0002']":
            th = threading.Thread(target=gpio_control.forward, daemon=True)
            th.start()

        elif DATA == "['0003']":
            th = threading.Thread(target=gpio_control.right, daemon=True)
            th.start()

        elif DATA == "['0004']":
            th = threading.Thread(target=gpio_control.reverse, daemon=True)
            th.start()

        elif DATA == "['0005']":
            break
        else:
            pass

        #clock += 1
        #if clock == 10:
            #th = threading.Thread(sensors.post(), daemon=True)
            #clock = 0


