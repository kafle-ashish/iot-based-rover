import RPi.GPIO as gpio
import time as t

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)
def forward():
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    t.sleep(4)
def reverse():
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    gpio.cleanup()
    t.sleep(2)
print("forward")
forward()
print("backward")
reverse()
gpio.cleanup()
