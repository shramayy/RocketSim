# First adding a timer for rocket launch
# Simulate flight under gravity and external thrust by engine

import math
import time


t = 0.1
h = 0
g = 9.806
dt = 0.1 
v =  0
fuelrate = float(input("Enter the rate of fuel ejection in kg/s: "))
fuelmass = float(input("Enter mass of fuel in rocket in kg: "))
rocketmass = float(input("Enter mass of rocket body in kg: "))
thrust = float(input("Enter thrust from rocket engine: "))
minthrust = (fuelmass + rocketmass)*g
ltime = 4
if thrust > (rocketmass+fuelmass)*g:
    liftoff = True
else: 
    liftoff = False

print ("All systers online")
time.sleep(1)
print ("Initiating launch sequence")
time.sleep(1)
print ("Engaging thrusters")
time.sleep(1)

print ("The rocket will launch in T-minus ")
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
    fuelmass = max(0, fuelmass - fuelrate*dt)
    totalmass = rocketmass + fuelmass 
    if fuelmass <=0:
        thrust = 0

    Fnet = thrust - totalmass*g
    a = Fnet/totalmass
    v += a*dt
    h += v*dt 
    
    if h <= 0:
        break

    print (f"Time: {t:.1f} | "
           f"Velocity: {v:.1f} | "
           f"Altitude: {h:.1f} | "
           f"Remaining fuel: {fuelmass} " 
    )
    t += dt

    
    
if not liftoff:
    time.sleep(1)
    print ("You selected an improper mass/thrust ratio. The net force on rocket is 'Fnet = thrust - mg'. If thrust is less than mg, then the rocket will not fly as "
    f"there is no acceleration in upward direction. Try changing the thrust to a value higher than {minthrust:.1f} if you intend to keep the same mass.")
    