# Simple demo of of the PCA9685 PWM servo/LED controller library.

import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 200  # Min pulse length out of 4096
servo_max = 500  # Max pulse length out of 4096
servo_mid = 300
speed = 0.2      #servo speed
speed1 = 0.5     #servo speed1

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)
def robotInitial():
    for i in range(12):
      pwm.set_pwm(i, 0, servo_mid)
      time.sleep(0.1)

def standLeg1():
    pwm.set_pwm(6, 0, 400)
    time.sleep(0.1)
    
    pwm.set_pwm(8, 0, 150)
    time.sleep(0.1)
    
    pwm.set_pwm(7, 0, 300)
    time.sleep(0.1)
    
def standLeg2():
    pwm.set_pwm(3, 0, 200)
    time.sleep(0.1)
    
    pwm.set_pwm(5, 0, 500)
    time.sleep(0.1)
    
    pwm.set_pwm(4, 0, 300)
    time.sleep(0.1)
    
def standLeg3():
    pwm.set_pwm(9, 0, 200)
    time.sleep(0.1)
    
    pwm.set_pwm(11, 0, 450)
    time.sleep(0.1)
    
    pwm.set_pwm(10, 0, 300)
    time.sleep(0.1)
    
def standLeg4():
    pwm.set_pwm(0, 0, 400)
    time.sleep(0.1)
    
    pwm.set_pwm(2, 0, 120)
    time.sleep(0.1)
    
    pwm.set_pwm(1, 0, 300)
    time.sleep(0.1)

def legs1():
    pwm.set_pwm(7, 0, 200)
    time.sleep(0.1)
    standLeg1()
    
    
def legs2():
    pwm.set_pwm(4, 0, 400)
    time.sleep(0.1)
    standLeg2()
   
    
def legs3():
    pwm.set_pwm(10, 0, 400)
    time.sleep(0.1)
    standLeg3()
    
    
def legs4():
    pwm.set_pwm(1, 0, 200)
    time.sleep(0.1)
    standLeg4()
    

def standUp():
    legs1()
    legs2()
    legs3()
    legs4()
    
def goLeg():
     #leg动作
    pwm.set_pwm(1, 0, 380)
    pwm.set_pwm(2, 0, 250)
    time.sleep(0.2)
    
    pwm.set_pwm(4, 0, 210)
    pwm.set_pwm(5, 0, 350)
    time.sleep(0.2)
    
    pwm.set_pwm(7, 0, 380)
    pwm.set_pwm(8, 0, 250)
    time.sleep(0.2)
    
    pwm.set_pwm(10, 0, 230)
    pwm.set_pwm(11, 0, 350)
    
    
#    pwm.set_pwm(2, 0, 250)
#    pwm.set_pwm(5, 0, 350)
#    pwm.set_pwm(8, 0, 250)
#    pwm.set_pwm(11, 0, 350)
#    
#    time.sleep(0.2)
#    
#    pwm.set_pwm(1, 0, 380)
#    pwm.set_pwm(4, 0, 210)
#    pwm.set_pwm(7, 0, 400)
#    pwm.set_pwm(10, 0, 230)
#    
    
    
    time.sleep(0.2)
    
    
    
def goLeg2():
    pwm.set_pwm(3, 0,200)
    time.sleep(0.2)
    
def dance():
    #stand
   
    
    goLeg()
    time.sleep(0.2)
    
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
    
    goLeg()
    time.sleep(0.2)
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
    time.sleep(0.2)
    goLeg()
    
    
    
    
    
def turnLeft():
    #stand
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
    #012leg4
    pwm.set_pwm(1, 0, 250)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 500)
    time.sleep(speed)
    pwm.set_pwm(1, 0, 300)
    time.sleep(speed)
#    pwm.set_pwm(0, 0, 400)
#    time.sleep(speed)
    #345leg2
    pwm.set_pwm(4, 0, 350)
    time.sleep(speed)
    pwm.set_pwm(3, 0, 300)
    time.sleep(speed)
    pwm.set_pwm(4, 0, 300)
    time.sleep(speed)
#    pwm.set_pwm(3, 0, 200)
#    time.sleep(speed)
    #678leg1
    pwm.set_pwm(7, 0, 250)
    time.sleep(speed)
    pwm.set_pwm(6, 0, 500)
    time.sleep(speed)
    pwm.set_pwm(7, 0, 300)
    time.sleep(speed)
#    pwm.set_pwm(6, 0, 400)
#    time.sleep(speed)
    #91011leg3
    pwm.set_pwm(10, 0, 350)
    time.sleep(speed)
    pwm.set_pwm(9, 0, 300)
    time.sleep(speed)
    pwm.set_pwm(10, 0, 300)
    time.sleep(speed)
#    pwm.set_pwm(9, 0, 200)
#    time.sleep(speed)
    
    pwm.set_pwm(0, 0, 400)
    pwm.set_pwm(3, 0, 200)
    pwm.set_pwm(6, 0, 400)
    pwm.set_pwm(9, 0, 200)
    
def turnRight():
    #stand
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
    #012leg4
    pwm.set_pwm(1, 0, 250)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 300)
    time.sleep(speed)
    pwm.set_pwm(1, 0, 300)
    time.sleep(speed)
    #345leg2
    pwm.set_pwm(4, 0, 350)
    time.sleep(speed)
    pwm.set_pwm(3, 0, 100)
    time.sleep(speed)
    pwm.set_pwm(4, 0, 300)
    time.sleep(speed)
    #678leg1
    pwm.set_pwm(7, 0, 250)
    time.sleep(speed)
    pwm.set_pwm(6, 0, 300)
    time.sleep(speed)
    pwm.set_pwm(7, 0, 300)
    time.sleep(speed)
    #91011leg3
    pwm.set_pwm(10, 0, 350)
    time.sleep(speed)
    pwm.set_pwm(9, 0, 100)
    time.sleep(speed)
    pwm.set_pwm(10, 0, 300)
    time.sleep(speed)
    #turn around
    pwm.set_pwm(0, 0, 400)
    pwm.set_pwm(3, 0, 200)
    pwm.set_pwm(6, 0, 400)
    pwm.set_pwm(9, 0, 200)

def sayHello():
     #stand
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
    time.sleep(speed)
    pwm.set_pwm(9, 0, 250)
    time.sleep(speed)
    pwm.set_pwm(1, 0, 200)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 480)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 400)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 480)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 400)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 480)
    time.sleep(speed)
    pwm.set_pwm(0, 0, 400)
    time.sleep(speed)
     #stand
    standLeg1()
    standLeg2()
    standLeg3()
    standLeg4()
   
        
    
    
    

 
    
robotInitial()
   
time.sleep(1) 
standUp()

time.sleep(1)
dance()
time.sleep(1)
turnLeft()
time.sleep(1)
turnLeft()
time.sleep(1)
turnRight()
time.sleep(1)
turnRight()
time.sleep(1)
sayHello()









