import RPi.GPIO as gpio
import time as t

class GPIOControl():

    MOT_A_IN1 =17
    MOT_A_IN2 =22
    MOT_A_IN3 =23
    MOT_A_IN4 =24

    MOT_B_IN1 =26
    MOT_B_IN2 =19
    MOT_B_IN3 =13
    MOT_B_IN4 =27

    def __init__(self):    
        gpio.setmode(gpio.BCM)
        #MOTORDRIVER A
        gpio.setup(self.MOT_A_IN1, gpio.OUT)
        self.MOT_A_IN1_PWM = gpio.PWM(self.MOT_A_IN1, 50)
        self.MOT_A_IN1_PWM.start(0)

        gpio.setup(self.MOT_A_IN2, gpio.OUT)
        self.MOT_A_IN2_PWM = gpio.PWM(self.MOT_A_IN2, 50)
        self.MOT_A_IN2_PWM.start(0)
        
        gpio.setup(self.MOT_A_IN3, gpio.OUT)
        self.MOT_A_IN3_PWM = gpio.PWM(self.MOT_A_IN3, 50)
        self.MOT_A_IN3_PWM.start(0)
        
        gpio.setup(self.MOT_A_IN4, gpio.OUT)
        self.MOT_A_IN4_PWM = gpio.PWM(self.MOT_A_IN4, 50)
        self.MOT_A_IN4_PWM.start(0)
        
        #MOTORDRIVER B
        gpio.setup(self.MOT_B_IN1, gpio.OUT)
        self.MOT_B_IN1_PWM = gpio.PWM(self.MOT_B_IN1, 50)
        self.MOT_B_IN1_PWM.start(0)

        gpio.setup(self.MOT_B_IN2, gpio.OUT)
        self.MOT_B_IN2_PWM = gpio.PWM(self.MOT_B_IN2, 50)
        self.MOT_B_IN2_PWM.start(0)
        
        gpio.setup(self.MOT_B_IN3, gpio.OUT)
        self.MOT_B_IN3_PWM = gpio.PWM(self.MOT_B_IN3, 50)
        self.MOT_B_IN3_PWM.start(0)
        
        gpio.setup(self.MOT_B_IN4, gpio.OUT)
        self.MOT_B_IN4_PWM = gpio.PWM(self.MOT_B_IN4, 50)
        self.MOT_B_IN4_PWM.start(0)
        
    def wait(self):
        #self.init()
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)
        t.sleep(4)
        gpio.cleanup()

    def forward(self):
        #self.init()
        self.MOT_A_IN1_PWM.start(50)#gpio.output(self.MOT_A_IN1, True)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(50)#gpio.output(self.MOT_A_IN4, True)

        self.MOT_B_IN1_PWM.start(50)#gpio.output(self.MOT_B_IN1, True)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(50)#gpio.output(self.MOT_B_IN4, True)

        t.sleep(4)
        gpio.cleanup()

    def left(self):
        #self.init()
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(50)#gpio.output(self.MOT_A_IN4, True)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(50)#gpio.output(self.MOT_B_IN4, True)

        t.sleep(4)
        gpio.cleanup()

    def right(self):
        #self.init()
        self.MOT_A_IN1_PWM.start(50)#gpio.output(self.MOT_A_IN1, True)
        self.MOT_A_IN2_PWM.start(0)#gpio.output(self.MOT_A_IN2, False)
        self.MOT_A_IN3_PWM.start(0)#gpio.output(self.MOT_A_IN3, False)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(50)#gpio.output(self.MOT_B_IN1, True)
        self.MOT_B_IN2_PWM.start(0)#gpio.output(self.MOT_B_IN2, False)
        self.MOT_B_IN3_PWM.start(0)#gpio.output(self.MOT_B_IN3, False)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)

        t.sleep(4)
        gpio.cleanup()

    def reverse(self):
        #self.init()
        self.MOT_A_IN1_PWM.start(0)#gpio.output(self.MOT_A_IN1, False)
        self.MOT_A_IN2_PWM.start(50)#gpio.output(self.MOT_A_IN2, True)
        self.MOT_A_IN3_PWM.start(50)#gpio.output(self.MOT_A_IN3, True)
        self.MOT_A_IN4_PWM.start(0)#gpio.output(self.MOT_A_IN4, False)

        self.MOT_B_IN1_PWM.start(0)#gpio.output(self.MOT_B_IN1, False)
        self.MOT_B_IN2_PWM.start(50)#gpio.output(self.MOT_B_IN2, True)
        self.MOT_B_IN3_PWM.start(50)#gpio.output(self.MOT_B_IN3, True)
        self.MOT_B_IN4_PWM.start(0)#gpio.output(self.MOT_B_IN4, False)

        t.sleep(4)
        gpio.cleanup()
