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
        for i in range(len(self.forces)):
            netF += self.forces[i]
        return netF
    

    def changelength(self, length):
        self.length = length
    
    def changecArea(self, area):
        self.cArea = area
    
    def changeradius(self, r):
        self.radius = r
    
    def changeMod(self, mod):
        self.modulusOfE = mod

    def addEForce(self, force):
        self.forces.append(force)

    def addposition(self, pos):
        self.fPos.append(pos)

    
    def calculateElongation(self):
        return print(((self.netForce()*self.length)/((self.cArea)*self.modulusOfE)))