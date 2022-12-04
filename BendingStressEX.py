class Bending:
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
        if geometry = cylindrical:
        MInertia = (π*r^4)/4
        else
        beam.geometry = rectangular 
        MInertia = (1/12)*b*h^3
    
    MaxBendingStress = M*c/MInertia

Problem1 = Bending()