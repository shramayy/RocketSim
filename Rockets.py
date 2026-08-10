class Rockets:
    def __init__ (self, name, fuelrate, fuelmass, bodymass, thrust):
        self.name = name
        self.fuelrate = fuelrate
        self.fuelmass = fuelmass
        self.bodymass = bodymass
        self.thrust = thrust 

falcon = Rockets("Falcon 9", 2960, 507500, 60000, 7600000)
starship = Rockets("Starship", 21450, 4900000, 360000, 74400000)