from packages import control_fetch 
from packages import gpio_control
from packages.mjpg_streamer import streamer
import sensors

def looper():

    clock: int = 0
    while(True):
        #print("Getting data......")
        DATA = str(control_fetch.get_data())
        #print(DATA)
        if DATA == "['0000']":
            gpio_control.wait()

        elif DATA == "['0001']":            
            gpio_control.left()

        elif DATA == "['0002']":
            gpio_control.forward()
        
        elif DATA == "['0003']":
            gpio_control.right()
        
        elif DATA == "['0004']":
            gpio_control.reverse()
        
        else:
            gpio_control.wait()
        
        clock += 1
        if clock == 60:
            sensors.post()
            clock = 0
    return

if __name__ == "__main__":
    looper()
