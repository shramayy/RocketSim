# All units are SI (kg/s, kg, kg, N, m²)  

class Stages:
    def __init__ (self, fuelrate, fuelmass, bodymass, thrust):
        self.fuelrate = fuelrate
        self.fuelmass = fuelmass
        self.bodymass = bodymass
        self.thrust = thrust 

stage1 = Stages(2600, 418000, 27200, 7600000)
stage2 = Stages(280, 112000, 4500, 981000)
class Rockets:
    def __init__ (self, name, area, mass):
        self.name = name 
        self.area = area
        self.mass = mass
        self.stages = [stage1, stage2]
        self.current_stage = 0


    def crash(self):
        print(f"{self.name} has crashed because:")

    def liftoff(self):
        print(f"{self.name} has successfully achieved liftoff!")

    def nofuel(self):
        print(f"{self.name} has used up all its fuel reserves.")

        

falcon = Rockets("Falcon 9", 10.5, 31700)
