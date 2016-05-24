import pigpio
from astral import Astral
from datetime import datetime  

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

if now > sunrise and now < sunset:
    print "Sun is out"
    lights("on", light_pin, pi)
else:
    print "Sun is not out"
    lights("off", light_pin, pi)

print now
print sunset
print sunrise
