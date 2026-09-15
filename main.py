# First adding a timer for rocket launch
# Simulate flight under gravity and external thrust by engine
# Adding pre built rockets to watch perfect flight.
# Adding velocity-time and altitude-time graphs.
# Adding drag with variable density and gravity, and constant C

import matplotlib.pyplot as plt
import math
import time
import random 
from Rockets import falcon, starship, saturn


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
time.sleep(1)

t = 0.1
h = 0
g0 = 9.806
rho0 = 1.225
radius = 6371000
c = 0.3
dt = 0.1 
v =  0
wind_v = random.randint(0, 30)
time_data = []
altitude_data = []
velocity_data = []
drag_data = []

minthrust = (rocket.fuelmass + rocket.bodymass)*g0
ltime = 4
if rocket.thrust > (rocket.fuelmass+rocket.bodymass)*g0:
    liftoff = True
else: 
    liftoff = False
    
print (f"You have chosen {rocket.name}. Flight will begin shortly.")
time.sleep(1)
print (f"Winds blowing at {wind_v} m/s.")
time.sleep(1)
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
    rho = rho0*math.exp(-h/8500)
    drag = 0.5 *rho*c*rocket.area*(v**2)
    g = g0*(radius / (radius + h))**2
    if rocket.fuelmass <=0:
        thrust = 0

    Fnet = thrust - totalmass*g - drag
    a = Fnet/totalmass
    v = math.sqrt((v + a*dt)**2 + wind_v**2)
    h += v*dt 
    
    if rocket.fuelmass <= 0:
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
    drag_data.append(drag)

plt.plot(time_data, velocity_data)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title(f"{rocket.name} : Velocity vs Time")

plt.show()


    
    
if not liftoff:
    time.sleep(1)
    print ("You selected an improper mass/thrust ratio. The net force on rocket is 'Fnet = thrust - mg'. If thrust is less than mg, then the it will not fly as "
    f"there is no acceleration in upward direction. Try changing the thrust to a value higher than {minthrust:.1f} if you intend to keep the same mass.")




