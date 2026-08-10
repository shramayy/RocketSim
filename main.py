# First adding a timer for rocket launch
# Simulate flight under gravity and external thrust by engine

import math
import time
from Rockets import falcon, starship

print ("Choose the rocket that will be taking flight today. Your options are:")
print ("1. Falcon 9")
print ("2. Starship")
print ("3. pass")
print ("4. pass")
print ("5. Custom")
choice = input("Enter the serial number of the rocket you'd like to test:")
if choice == "1" :
    rocket = falcon
    
elif choice == "2" :
    rocket = starship

elif choice == "5" :
    name = input ("Enter a name for your rocket: ")
    fuelrate = float(input("Enter the rate of fuel ejection in kg/s: "))
    fuelmass = float(input("Enter mass of fuel in rocket in kg: "))
    bodymass = float(input("Enter mass of rocket body in kg: "))
    thrust = float(input("Enter thrust from rocket engine: "))

else:
    print("That is an invalid choice.")

print (f"You have chosen {rocket.name}. Flight will begin shortly.")
t = 0.1
h = 0
g = 9.806
dt = 0.1 
v =  0
minthrust = (rocket.fuelmass + rocket.bodymass)*g
ltime = 4
if rocket.thrust > (rocket.fuelmass+rocket.bodymass)*g:
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
    rocket.fuelmass = max(0, rocket.fuelmass - rocket.fuelrate*dt)
    totalmass = rocket.bodymass + rocket.fuelmass
    if rocket.fuelmass <=0:
        thrust = 0

    Fnet = rocket.thrust - totalmass*g
    a = Fnet/totalmass
    v += a*dt
    h += v*dt 
    
    if h <= 0:
        break

    print (f"Time: {t:.1f} | "
           f"Velocity: {v:.1f} | "
           f"Altitude: {h:.1f} | "
           f"Remaining fuel: {rocket.fuelmass} " 
    )
    t += dt

    
    
if not liftoff:
    time.sleep(1)
    print ("You selected an improper mass/thrust ratio. The net force on rocket is 'Fnet = thrust - mg'. If thrust is less than mg, then the it will not fly as "
    f"there is no acceleration in upward direction. Try changing the thrust to a value higher than {minthrust:.1f} if you intend to keep the same mass.")
    