class beam():
    def __init__(self):
        self.length = None
        self.cArea = None
        self.radius = None
        self.height = 1
        self.depth = 1
        self.modulusOfE = 20
        self.forces = []
        self.fPos = []

    def netForce(self):
        netF = 0
        for force in self.forces:
            netF += force
        return netF
    
    def calculateElongation(self):
        return ((self.netForce(self.forces)*self.length)/((self.depth*self.height)*self.modulusOfE))