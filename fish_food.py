import pigpio
import time

#config
food_pin = 17
turns = 2

# initializing
pi = pigpio.pi()
pi.set_servo_pulsewidth(food_pin, 1000)
time.sleep(0.91)
pi.set_servo_pulsewidth(food_pin, 0)

