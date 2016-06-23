import pigpio
from astral import Astral
from datetime import datetime  
from datetime import time

#config
light_pin = 5

# initializing
pi = pigpio.pi()
a = Astral()
a.solar_depression = 'civil'
city = a['Washington DC']

def lights(action="on", pin=5, p=None):
    if action == "on":
        p.write(pin, 0)
    elif action == "off":
        p.write(pin, 1)    
    return

# check if the sun is out
sunrise, sunset = city.daylight()
now = datetime.now(city.tzinfo)

if now.isoweekday() < 6:
    if now.time() > time(7, 0, 0) and now.time() < sunset.time():
        lights("on", light_pin, pi)
    else:
        lights("off", light_pin, pi)
else:
    if now.time() > time(9, 0, 0) and now.time() < sunset.time():
        lights("on", light_pin, pi)
    else:
        lights("off", light_pin, pi)
