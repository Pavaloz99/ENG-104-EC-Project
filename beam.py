class beam():
    def __init__(self):
        self.length = None
        self.cArea = None
        self.radius = None
        self.height = 1
        self.depth = 1
        self.modulusOfE = 20
        self.forces = []
        self.tForces = {}
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

    def addtForce(self, force, pos):
        if(self.tForces[str(pos)]):
            tempArry = list(self.tForces[str(pos)])
            self.tForces.update({str(pos): tempArry.append(force)})

        else:
            self.tForces[str(pos)] = force
    
    def torsionCalc(self):
        #forces should be given as "+" for out of page and "-" for into page
        #position for this case will be in the y-dir relative to the bar
        #torque in one position x along the bar
        torque = [
            []
            ]
        tpositionAlongX = self.tForces.keys()

        for i in range(len(self.tForces)):
            position = self.tForces[str(tpositionAlongX[i])]
            for k in range(len(self.tForces[str(position)])):
                
        
            

    def calculateElongation(self):
        return print(((self.netForce()*self.length)/((self.cArea)*self.modulusOfE)))