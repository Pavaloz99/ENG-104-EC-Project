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

