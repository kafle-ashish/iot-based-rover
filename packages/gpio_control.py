import RPi.GPIO as gpio
import time as t

MOT_A_IN1 =17
MOT_A_IN2 =22
MOT_A_IN3 =23
MOT_A_IN4 =24

MOT_B_IN1 =26
MOT_B_IN2 =19
MOT_B_IN3 =13
MOT_B_IN4 =27

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)

    gpio.setup(26,gpio.OUT)
    gpio.setup(19,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(27,gpio.OUT)

def wait():
    init()
    gpio.output(17,False)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,False)

    gpio.output(26,False)
    gpio.output(19,False)
    gpio.output(13,False)
    gpio.output(27,False)
    t.sleep(4)
    gpio.cleanup()

def forward():
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)

    gpio.output(26,True)
    gpio.output(19,False)
    gpio.output(13,False)
    gpio.output(27,True)

    t.sleep(4)
    gpio.cleanup()

def left():
    init()
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)

    gpio.output(26,False)
    gpio.output(19,False)
    gpio.output(13,False)
    gpio.output(27,True)

    t.sleep(4)
    gpio.cleanup()

def right():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)

    gpio.output(26,True)
    gpio.output(19,False)
    gpio.output(13,False)
    gpio.output(27,False)

    t.sleep(4)
    gpio.cleanup()

def reverse():
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)

    gpio.output(26,False)
    gpio.output(19,True)
    gpio.output(23,True)
    gpio.output(27,False)

    t.sleep(4)
    gpio.cleanup()
