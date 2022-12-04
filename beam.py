import numpy as np

class beam():
    def __init__(self):
        self.length = None
        self.cAreaConst = None
        self.radius = None
        self.height = 1
        self.depth = 1
        self.modulusConst = None
        self.cAreaChanging = {} 
        self.sections = {}
        self.modulusChagning = {}
        self.forces = []
        self.tForces = {}
        self.fPos = []
        self.compatibility = None
        self.forceEq = None

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
        torque = {}
        tpositionAlongX = list(self.tForces)
        
        for pos in self.tForces:
            force = self.tForces[pos][0]
            print (force)
            k = 1
            netT = 0
            for k in range(len(self.tForces[pos])):
                netT += force * (self.tForces[pos][k]) ##this is where I left off debugging
            torque.update({str(pos): netT})
            #Polar Moment
            
            diameter = np.sqrt((self.cArea*4)/(np.pi))

            J = (np.pi/32)*((diameter)**4)
            
        Tau = {}
        # angleOfTwist = {}  

        for pos in torque:
            Tau.update({str(pos): torque[pos]*(diameter/(2*1000))/J})
            

            # angleOfTwist[j][0] = (torque[j][0]*int(tpositionAlongX[j]))/((self.modulusOfG)(*J))
            # angleOfTwist[j][1] = torque[j][0]
        return[Tau]

    def axLoadIndRxnForces(self):
        if self.compatibility == 0:
            netForce = 0
            delta = []
            b = []
            superposition = 0
            forceTotal = 0
            for pos in range(len(self.fPos)):
                forceTotal = 0
                ##first delta
                if pos == 0:
                    delta.append(self.fPos[pos])
                    forceTotal += self.forces[pos]
                #last delta
                if pos == len(self.fPos)-1:
                    delta.append((self.length - self.fPos[pos]))
                    b.append(-superposition)
                #Adding all middle contributions
                else:
                    
                    superposition += forceTotal*self.fPos[pos]
                    forceTotal += self.forces[pos]
                
            self.a = np.array([[1,-1],delta]) 
            self.forceEq = np.array([-sum(self.forces), superposition])


            return print(np.linalg.solve(self.a,self.forceEq))
           
        
            




        
            

    def calculateElongation(self):
        return ((self.netForce()*self.length)/((self.cArea)*self.modulusOfE))