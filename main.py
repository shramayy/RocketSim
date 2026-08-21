# First adding a timer for rocket launch
# Simulate flight under gravity and external thrust by engine
# Adding pre built rockets to watch perfect flight.
# Adding velocity-time and altitude-time graphs.
# Adding drag with constant density and C

import matplotlib.pyplot as plt
import pygame
import time
from Rockets import falcon, starship, saturn

pygame.init()

print ("Choose the rocket that will be taking flight today. Your options are:")
print ("1. Falcon 9")
print ("2. Starship")
print ("3. Saturn 5")
print ("4. pass")
print ("5. Custom")
choice = input("Enter the serial number of the rocket you'd like to test:")
if choice == "1" :
    rocket = falcon
    
elif choice == "2" :
    rocket = starship

elif choice == "3" :
    rocket = saturn

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
rho = 1.225
Cd = 0.3
dt = 0.1 
v =  0
time_data = []
altitude_data = []
velocity_data = []

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
    rocket.liftoff()
else:
    rocket.crash()

while liftoff:
    thrust = rocket.thrust
    rocket.fuelmass = max(0, rocket.fuelmass - rocket.fuelrate*dt)
    totalmass = rocket.bodymass + rocket.fuelmass
    drag = 0.5 *rho*Cd*rocket.area*(v**2)
    if rocket.fuelmass <=0:
        thrust = 0

    Fnet = thrust - totalmass*g - drag
    a = Fnet/totalmass
    v += a*dt
    h += v*dt 
    
    if v <= 0:
        break

    print (f"Time: {t:.1f} | "
           f"Velocity: {v:.1f} | "
           f"Drag: {drag:.1f} | "
           f"Net Force: {Fnet:.1f} | "
           f"Altitude: {h:.1f} | "
           f"Remaining fuel: {rocket.fuelmass} " 
    )
    t += dt

    time_data.append(t)
    altitude_data.append(h)
    velocity_data.append(v)

plt.plot(time_data, velocity_data)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title(f"{rocket.name} : Velocity vs Time")

plt.show()


    
    
if not liftoff:
    time.sleep(1)
    print ("You selected an improper mass/thrust ratio. The net force on rocket is 'Fnet = thrust - mg'. If thrust is less than mg, then the it will not fly as "
    f"there is no acceleration in upward direction. Try changing the thrust to a value higher than {minthrust:.1f} if you intend to keep the same mass.")



