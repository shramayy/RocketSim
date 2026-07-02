#First adding a timer for rocket launch

import time

ltime = 10

print ("All systers online")
time.sleep(1)

print ("Initiating launch sequence")
time.sleep(1)

print ("Engaging thrusters")
time.sleep(1)

print ("The rocket will launch in T-minus 10 ")
time.sleep(1)

for x in reversed(range(1, ltime)):
    print (f"{x}")
    time.sleep(1)

#Then follows 2 different paths, where liftoff is achieved and not. 
