import RPi.GPIO as gpio
import time as t

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)
    return

def forward():
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    t.sleep(4)
    return

def reverse():
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    gpio.cleanup()
    t.sleep(2)
    return

def wait():
    pass

def left():
    pass

def right():
    pass

if __name__ == "__main__":
    init()
