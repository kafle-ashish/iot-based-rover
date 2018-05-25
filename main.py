from packages import get_control_data 
import multiprocessing
import gpio_control

def checker(DATA):
    if DATA == "0000":
        print(DATA)
    elif DATA == "0001":
        gpio_control.forward()
    elif DATA == "0002":
        print(DATA)
    elif DATA == "0003":
        print(DATA)
    elif DATA == "0004":
        print(DATA)
    elif DATA == "0005":
        print(DATA)
    else:
        print(DATA)
    return

def looper():
    global DATA
    while(True):
        #print("Getting data......")
        DATA = str(get_control_data.get_data())
        #to-do
        #Insert a function to handle garbage DATA 
        checker()

#looper()
checker("0001")
