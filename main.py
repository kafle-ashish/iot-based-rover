from packages import control_fetch 
from packages import gpio_control

def looper():
    while(True):
        #print("Getting data......")
        DATA = str(control_fetch.get_data())
        
        if DATA == "0000":
            gpio_control.wait()
        elif DATA == "0001":
            gpio_control.left()
        elif DATA == "0002":
            gpio_control.forward()
        elif DATA == "0003":
            gpio_control.right()
        elif DATA == "0004":
            gpio_control.reverse()
        else:
            gpio_control.wait()

    return

if __name__ == "__main__":
    looper()
