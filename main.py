import matplotlib.pyplot as plt
import math
import time
import random 
from Rockets import falcon, starship, saturn

print ("Choose the rocket that will be taking flight today:")
print ("1. Falcon 9")
print ("2. Starship")
print ("3. Saturn V")
while True:
    choice = input("Enter the serial number of the rocket you'd like to test:")
    if choice == "1" :
        rocket = falcon
        break
        
    elif choice == "2" :
        rocket = starship
        break

    elif choice == "3" :
        rocket = saturn
        break

    else:
        print("That is an invalid choice.")


# Defining Variables

t = 0
x = 0
h = 0
h_max = h
g0 = 9.806
rho0 = 1.225
radius = 6371000
c = 0.3
dt = 1 
v_y = 0
v_x = 0
wind_v = random.randint(-30, 30)
theta = math.radians(90)
turn_rate = math.radians(0.5)
time_data = []
altitude_data = []
xvelocity_data = []
yvelocity_data = []
nvelocity_data = []
drag_data = []
range_data = []
liftoff = True
burnout = False

time.sleep(1)

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

for x in reversed(range(1, 4)):
    print (f"{x}")
    time.sleep(1)
# Then follows 2 different paths, where liftoff is achieved and not. 

if liftoff:
    rocket.liftoff()
else:
    rocket.crash()

while liftoff and t<600:
    stage = rocket.stages[rocket.current_stage]
    if stage.fuelmass >0:
        thrust = stage.thrust
        stage.fuelmass = max(0, stage.fuelmass - stage.fuelrate*dt)

    else:
        thrust = 0

    totalmass = rocket.mass + sum(s.fuelmass for s in rocket.stages)
    rho = rho0*math.exp(-h/8500)
    drag_y = 0.5 *rho*c*rocket.area*abs(v_y)*v_y
    drag_x = 0.5*rho*c*rocket.area*((v_x - wind_v)*abs(v_x - wind_v))
    g = g0*(radius / (radius + h))**2

    Fnet_y = thrust*math.sin(theta) - totalmass*g - drag_y
    Fnet_x = thrust*math.cos(theta) - drag_x
    a_y = Fnet_y/totalmass
    a_x = Fnet_x/totalmass
    v_y += a_y*dt
    v_x += a_x*dt
    h += v_y*dt
    h_max = max(h, h_max)
    x += v_x*dt 
    v_net = math.sqrt(v_x**2 + v_y**2)

# Not realistic. Only for testing purposes.
    
    if h > 1500 and theta > math.radians(30):
        theta = max(math.radians(30), theta - turn_rate * dt)
        
    

    print (f"Time: {t:.1f} | "
        f"Velocity Y: {v_y:.1f} m/s | "
        f"Velocity X: {v_x:.1f} m/s | "
        f"Total Mass: {totalmass:.1f} | "
        f"Force Y: {Fnet_y:.1f} | "
        f"Thrust: {thrust:.1f} | "
        f"Altitude: {h:.1f} | "
        f"Range: {x:.1f} | "
        f"Remaining fuel: {stage.fuelmass:.1f} " 
    )

    t += dt
# Stage Separation
    if stage.fuelmass <= 0:
            if len(rocket.stages) - 1 > rocket.current_stage:
                print (f"Stage {rocket.current_stage + 1} has no remaining fuel.")
                rocket.mass -= stage.bodymass
                rocket.current_stage += 1
                print("Stage", rocket.current_stage + 1, "active")

            else: 
                if not burnout:
                    print("Final stage has run out of fuel")
                    burnout = True

                

            

    time_data.append(t)
    altitude_data.append(h/1000)
    xvelocity_data.append(v_x)
    yvelocity_data.append(v_y)
    nvelocity_data.append(v_net)
    drag_data.append(drag_y)
    range_data.append(x)


# Graphs

plt.plot(time_data, yvelocity_data, label="Altitude")
plt.xlabel("Time")
plt.ylabel("Altitude (km)")
plt.title(f"{rocket.name}: Altitude vs Time")
plt.show()


    
# minthrust = (stage.fuelmass + stage.bodymass)*g0
# if thrust < minthrust:
#     liftoff = False
# if not liftoff:
#     time.sleep(1)
#     print ("You selected an improper mass/thrust ratio. The net force on rocket is 'Fnet = thrust - mg'. If thrust is less than mg, then the it will not fly as "
#     f"there is no acceleration in upward direction. Try changing the thrust to a value higher than {minthrust:.1f} if you intend to keep the same mass.")




