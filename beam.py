import numpy as np

class beam():
    def __init__(self):
        self.length = None
        self.cArea = None
        self.radius = None
        self.height = 1
        self.depth = 1
        self.modulusOfE = 20
        self.modulusOfG = 80000000000
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
        if(pos in self.tForces):
            tempArry = list().append(self.tForces[str(pos)])
            self.tForces.update({str(pos): tempArry.append(force)})

        else:
            self.tForces[str(pos)] = force
    
    def torsionCalc(self):
        #forces should be given as "+" for out of page and "-" for into page
        #position for this case will be in the y-dir relative to the bar
        #torque in one position x along the bar
        torque = []
        tpositionAlongX = list(self.tForces)
        
        for i in range(len(self.tForces)):
            position = str(tpositionAlongX[i])
            force = self.tForces[str(position)][0] if type(self.tForces[str(position)]) is type(list()) else self.tForces[str(position)]
            k = 1
            
            for k in range(len(self.tForces)):
                torque[i][0] += force * self.tForces[str(position)][k] ##this is where I left off debugging
            
            torque[i][1] = position 
            #Polar Moment
            
            diameter = np.sqrt((self.cArea*4)/(np.pi))

            J = (np.pi/32)*((diameter)**4)
            
        Tau = []
        angleOfTwist = []
        netT = 0 
        for t in torque:
            netT += torque[t][0]
        torque.insert(0, [-netT,0])  

        for j in range(len(torque)):
            Tau[j][0] = (torque[j][0]*(diameter/(2*1000)))/J
            Tau[j][1] = torque[j][1]

            angleOfTwist[j][0] = (torque[j][0]*int(tpositionAlongX[j]))/((self.modulusOfG)(*J))
            angleOfTwist[j][1] = torque[j][0]
        return[Tau, angleOfTwist]

        
        
            




        
            

    def calculateElongation(self):
        return print(((self.netForce()*self.length)/((self.cArea)*self.modulusOfE)))