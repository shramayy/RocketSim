# First adding a timer for rocket launch
# Simulate flight under gravity and external thrust by engine

import math
import time


t = 0.1
h = 0
g = 9.806
dt = 0.1 
v =  0
fuelrate = 10
fuelmass = 2000
rocketmass = 4000
thrust = 75000
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

while liftoff:
    fuelmass -= fuelrate*dt
    totalmass = rocketmass + fuelmass 
    Fnet = thrust - totalmass*g
    a = Fnet/totalmass
    v += a*dt
    h += v*dt 

    print (f"Time: {t:.1f} | "
           f"Velocity: {v:.1f} | "
           f"Altitude: {h:.1f} | "
           f"Remaining fuel: {fuelmass} | " 
           f"Total mass: {totalmass} "
    )
    time.sleep(0.1)
    t += dt

    if t>=5:
        break


    