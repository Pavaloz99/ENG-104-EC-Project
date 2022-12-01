from beam import beam

### Example based off of HW # 5 Problem 5 ###

#Calculates the maximum internal bending moment
def bending(beam): 
    maxMoment = 0

    #loops through beam by one increment and calulates moment at each cut, returns max moment
    for i in range (beam.length):
        moment = 0
        #loop that goes through each force
        for k in range(len(beam.forces)):
            if beam.fPos[k] < i: #Compares current position by index to the position of each force, so that only the forces to the left are consideresd
                distance = i - beam.fPos[k]
                moment += beam.forces[k] * distance
            else: 
                break
        if abs(moment) > maxMoment:
            maxMoment = moment

    return maxMoment


myBeam = beam()
myBeam.length = 2500
myBeam.forces = [-200,625,-350,-400,525,-200]
myBeam.fPos = [0, 500, 900 ,1500,2100,2500]


#result needs to converted from N*mm -> N*m
print(bending(myBeam)/1000)

# for cylindrical beam
def __init__ (self, r):
    self.r = r #radius

# for rectangular beam
def __init__ (self, b, h):
    self.b = b #base
    self.h = h #height

# for max bending stress
def __init__ (self, M, c):
    self.M = M # Resultant internal moment
    self.c = c # perpendicular distance from the neutral axis to a point farthest away from the neutral axis
    self.MInertia = {}

def BendingStress():
    # cylindrical or rectangular beam. compute moment of intertia for the beam. then max bending stress
    if beam.geometry = cylindrical 
        MInertia = (π*r^4)/4
        else
        beam.geometry = rectangular 
        MInertia = (1/12)*b*h^3
    
    MaxBendingStress = M*c/MInertia
    
