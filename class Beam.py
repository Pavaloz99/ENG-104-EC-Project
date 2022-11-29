class Beam():
#constructor for Axial Load Statically det 
def __init__(self, L, E, A, P):
    self.L = L #length
    self.E = E #Modulus of Elasticity
    self.A = A #Area
    self.P = P #Applied Load
    self.Force = {}

#constructor for Axial Load Statically ind
def __init__(self, L, E, A):
    self.L = L #length
    self.E = E #Modulus of Elasticity
    self.A = A #Area
    self.P = {} #Applied Load in Each Section
    self.Force = {}

#constructor for Torsion stat det
def __init__(self, J):
    self.J = J #Polar Moment of Intertia
    self.Force = {}
    self.T = {} #Internal Torque
    self.c = {} #Outer Radius

