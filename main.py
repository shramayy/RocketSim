# First adding a timer for rocket launch
# Starting with calculating velocity at various stages using the Ideal Rocket Equation

import math
import time

fuelmass = float(input("Mass of fuel in rocket: "))
rocketbody = float(input("Mass of rocket body: "))
usedfuel = float(input("Amount of the fuel used until this instant: "))
while usedfuel > fuelmass:
    print("Amount of fuel burnt can not be more than fuel initially in the rocket.")
    usedfuel = float(input("Amount of the fuel used until this instant: "))

imass = fuelmass + rocketbody 
u = float(input("Velocity of fuel ejection: "))
fmass = imass - usedfuel
fspeed = u * math.log(imass/fmass)
ltime = 3
liftoff = True
print ("All systers online")
time.sleep(1)
print ("Initiating launch sequence")
time.sleep(1)

print ("Engaging thrusters")
time.sleep(1)

print ("The rocket will launch in T-minus 3 ")
time.sleep(1)

for x in reversed(range(1, ltime)):
    print (f"{x}")
    time.sleep(1)

#Then follows 2 different paths, where liftoff is achieved and not. 
if liftoff:
    print ("Liftoff, adios!")
else:
    print ("Whoops, there it goes..... right into the water. Try again next time.")

print (f"The speed of rocket right now is {fspeed} km/s") 
    