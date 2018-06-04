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
    gpio.setup(MOT_A_IN1, gpio.OUT)
    gpio.setup(MOT_A_IN2, gpio.OUT)
    gpio.setup(MOT_A_IN3, gpio.OUT)
    gpio.setup(MOT_A_IN4, gpio.OUT)

    gpio.setup(MOT_B_IN1, gpio.OUT)
    gpio.setup(MOT_B_IN2, gpio.OUT)
    gpio.setup(MOT_B_IN3, gpio.OUT)
    gpio.setup(MOT_B_IN4, gpio.OUT)

def wait():
    init()
    gpio.output(MOT_A_IN1, False)
    gpio.output(MOT_A_IN2, False)
    gpio.output(MOT_A_IN3, False)
    gpio.output(MOT_A_IN4, False)

    gpio.output(MOT_B_IN1, False)
    gpio.output(MOT_B_IN2, False)
    gpio.output(MOT_B_IN3, False)
    gpio.output(MOT_B_IN4, False)
    t.sleep(4)
    gpio.cleanup()

def forward():
    init()
    gpio.output(MOT_A_IN1, True)
    gpio.output(MOT_A_IN2, False)
    gpio.output(MOT_A_IN3, False)
    gpio.output(MOT_A_IN4, True)

    gpio.output(MOT_B_IN1, True)
    gpio.output(MOT_B_IN2, False)
    gpio.output(MOT_B_IN3, False)
    gpio.output(MOT_B_IN4, True)

    t.sleep(4)
    gpio.cleanup()

def left():
    init()
    gpio.output(MOT_A_IN1, False)
    gpio.output(MOT_A_IN2, False)
    gpio.output(MOT_A_IN3, False)
    gpio.output(MOT_A_IN4, True)

    gpio.output(MOT_B_IN1, False)
    gpio.output(MOT_B_IN2, False)
    gpio.output(MOT_B_IN3, False)
    gpio.output(MOT_B_IN4, True)

    t.sleep(4)
    gpio.cleanup()

def right():
    init()
    gpio.output(MOT_A_IN1, True)
    gpio.output(MOT_A_IN2, False)
    gpio.output(MOT_A_IN3, False)
    gpio.output(MOT_A_IN4, False)

    gpio.output(MOT_B_IN1, True)
    gpio.output(MOT_B_IN2, False)
    gpio.output(MOT_B_IN3, False)
    gpio.output(MOT_B_IN4, False)

    t.sleep(4)
    gpio.cleanup()

def reverse():
    init()
    gpio.output(MOT_A_IN1, False)
    gpio.output(MOT_A_IN2, True)
    gpio.output(MOT_A_IN3, True)
    gpio.output(MOT_A_IN4, False)

    gpio.output(MOT_B_IN1, False)
    gpio.output(MOT_B_IN2, True)
    gpio.output(MOT_B_IN3, True)
    gpio.output(MOT_B_IN4, False)

    t.sleep(4)
    gpio.cleanup()
