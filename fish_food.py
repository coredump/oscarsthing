#!/usr/bin/env python

import pigpio
import time

#config
food_pin = 17
turns = 3

# positions
center = 1500
cw = 500
ccw = 2500

# initializing
pi = pigpio.pi()

def shake_it(pin, shakes = 2):
    # center the stem
#    print "initial center"
#    pi.set_servo_pulsewidth(pin, center)
#    time.sleep(2)

    print "ccw"
    pi.set_servo_pulsewidth(pin, ccw)
    time.sleep(0.5)
    print "cw"
    pi.set_servo_pulsewidth(pin, cw)
    time.sleep(1.5)

#    pi.set_servo_pulsewidth(pin, center)
#    time.sleep(3)
    return

# shake it
print "Shaking"
for i in range(0, turns):
    shake_it(food_pin)

pi.set_servo_pulsewidth(food_pin, 0)

