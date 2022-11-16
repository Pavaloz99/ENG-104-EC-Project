class beam():
    def __init__(self):
        self.length = None
        self.cArea = None
        self.radius = None
        self.height = None
        self.depth = None
        self.modulusOfE = 20
        self.forces = []

    def netForce(self):
        netF = 0
        for force in self.forces:
            netF += force
        return netF
    
    def calculateElongation(self):
        return ((self.netForce(self.forces)*self.length)/((self.depth*self.height)*self.modulusOfE))