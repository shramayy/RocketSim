# Rocket Simulation

## What is it?

It began as an attempt at a simulator to teach others how rockets achieve liftoff and make it to space. However, keeping the simulative essence intact, it will now serve as a generator of data for a model to predict max altitude and many other labels knowing which is essential because of their importance in flight planning. 

## Why is it?

This program exists because I love rockets, and I want to share that fascination with the rest of the world. I made this to satiate my curiosity and to catch a glance of what space exploration begins with.

## Main functions

Simulates flights under the effect of gravity, atmospheric drag, wind and atmosphere. A model is to be created which will use data from simulated flights with changing parameters to find out values like max altitude, max velocity, time of flight, etc. 

## Order of things done

1. Added launch timer.
2. Rocket simulated under the effect of gravity and external thrust. 
3. Added existing rocket specifications.
4. Added velocity-time and altitude-time graphs.
5. Added drag with drag coefficient (C<sub>D</sub>) and variable air density 
6. Added a display with a rocket and background.
7. Fixed bugs and added staging.


## Issues faced

1. Not enough thrust in comparison to rocket mass kept printing the velocity and altitude to be negative. (resolved)
2. The rocket instantly loses fuel before any movement. (resolved)
3. Staging. The entireity of it.
4. Unusual velocity and altitude peaks. 



## Disclaimer

This simulator is an educational project, not a validated aerospace engineering tool. Its predictions depend on the assumptions and approximations used in the physics model.

Atmospheric modeling, aerodynamic effects, guidance, propulsion, staging, and orbital dynamics may be simplified or incomplete. Simulated results should not be interpreted as validated predictions of real launch vehicles.



##                                             IN DEVELOPMENT