# All units are SI (kg/s, kg, kg, N, m²)  

class Stages:
    def __init__ (self, name, fuelrate, fuelmass, bodymass, thrust):
        self.name = name
        self.fuelrate = fuelrate
        self.fuelmass = fuelmass
        self.bodymass = bodymass
        self.thrust = thrust 

fstage1 = Stages("Stage 1", 2600, 418000, 27200, 7600000)
fstage2 = Stages("Stage 2", 280, 112000, 4500, 981000)
ststage1 = Stages("Stage 1", 22800, 3650000, 300000, 80900000)
ststage2 = Stages("Stage 2", 4000, 1600000, 110000, 15450000)
sstage1 = Stages("Stage 1", 13500, 2160000, 131500, 33360000)
sstage2 = Stages("Stage 2", 1314, 473000, 38400, 5004000)
sstage3 = Stages("Stage 3", 238, 107000, 15200, 1023000) 
class Rockets:
    def __init__ (self, name, area, stages, mass):
        self.name = name 
        self.area = area
        self.mass = mass
        self.stages = stages
        self.current_stage = 0


    def crash(self):
        print(f"{self.name} has crashed because:")

    def liftoff(self):
        print(f"{self.name} has successfully achieved liftoff!")

    def nofuel(self):
        print(f"{self.name} has used up all its fuel reserves.")

        

falcon = Rockets("Falcon 9", 10.5, [fstage1, fstage2], 31700)
starship = Rockets("Starship", 63.6, [ststage1, ststage2], 410000)
saturn = Rockets("Saturn V", 80.1, [sstage1, sstage2, sstage3], 185100)