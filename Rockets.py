# All units are SI (kg/s, kg, kg, N, m²)  
class Rockets:
    def __init__ (self, name, fuelrate, fuelmass, bodymass, thrust, area):
        self.name = name
        self.fuelrate = fuelrate
        self.fuelmass = fuelmass
        self.bodymass = bodymass
        self.thrust = thrust 
        self.area = area

    def crash(self):
        print(f"{self.name} has crashed because:")

    def liftoff(self):
        print(f"{self.name} has successfully achieved liftoff!")

    def nofuel(self):
        print(f"{self.name} has used up all its fuel reserves.")

falcon = Rockets("Falcon 9", 2960, 507500, 60000, 7600000, 10.5)
starship = Rockets("Starship", 21450, 4900000, 360000, 74400000, 63.6)
saturn = Rockets("Saturn 5", 15000, 2077000, 137000, 34500000, 80.1)