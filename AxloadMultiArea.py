# For Compatibility = 0
# For change in area = 1
# Same elastic modulus

import numpy as np

print("What is the compatibility condition for this problem? (meters)")
delta = float(input())


NumbersA = 1

if NumbersA == 1:

    print("How many forces act upon the rightmost beam?")
    NumbersFright = int(input())
    print("What are the values of these forces in Newtons? (Positive if it points right)")
    ForceArrayRight = np.empty(NumbersFright)

    for i in range(NumbersFright):
        ForceArrayRight[i] = float(input())

    print("How many forces act upon the leftmost beam?")
    NumbersFleft = int(input())
    print("What are the values of these forces in Newtons? (Positive if it points right)")
    ForceArrayLeft = np.empty(NumbersFleft)

    for i in range(NumbersFleft):
        ForceArrayLeft[i] = float(input())
    
    print("What is the length of the entire compound beam in meters?")
    Dfull = float(input())

    print("What is the length of the leftmost beam in meters?")
    Lr2 = float(input())

    print("What is the length of the rightmost beam in meters?")
    Lr1 = float(input())

    print("If the change in area location is referenced as x = 0 meters, what are the distances in meters from the reference to each force that act upon the beam to the right of x = 0? (positive values only)")
    print("Start with the closest force to reference.")
    dr = np.empty(NumbersFright)

    for i in range(NumbersFright):
        dr[i] = float(input())


    print("If the change in area location is referenced as x = 0 meters, what are the distances in meters from the reference to each force that act upon the beam to the left of x = 0? (positive values only)")
    print("Start with the closest force to reference.")
    dl = np.empty(NumbersFleft)

    for i in range(NumbersFleft):
        dl[i] = float(input())


    print("Cross sectional area of leftmost portion of the beam in square meters.")
    r2 = float(input())

    print("Cross sectional area of rightmost portion of the beam in square meters.")
    r1 = float(input())

    NumbersF = NumbersFleft + NumbersFright

    # part of numerator for rightmost reaction force equation
    varx = 0
    partNmtrArray1 = np.empty(NumbersFright)
    for i in range(NumbersFright):
        varx = i
        partNmtrArray1[i] = dr[i] * ForceArrayRight[i]
    partNmtr1 = sum(partNmtrArray1)

    partNmtrArray2 = np.empty(NumbersFleft)
    for i in range(NumbersFleft):
        varx = i
        partNmtrArray2[i] = dr[i] * ForceArrayLeft[i]
    
    ratio = r1/r2

    partNmtrArray2 = partNmtrArray2/ratio
    partNmtr2 = sum(partNmtrArray2)

    partT = partNmtr1 + partNmtr2

    PTot = sum(ForceArrayLeft) + sum(ForceArrayRight) # Sum of all external axial loads


cc = NumbersF + 2 # Amount of segments
jj = NumbersF # Last array value index
LengthSeg = np.empty(cc)

if delta == 0:
    if NumbersA == 1:
        
        # Solve for Fa - rightmost reaction force
        Fa = (r2*Lr1*PTot - r2*partT) / (r2*Lr1 - r1*Lr2)
        Fb = r1*Lr2*((Lr1*PTot - partT)/(r2*Lr1 - r1*Lr2))

        print("Fa = " + str(Fa) + " Newtons")
        print("Fb = " + str(Fb) + " Newtons")
        print("*If F is positive, reaction points right. If F is negative, reaction points left.")
        print("Fa located at far left of beam and Fb located at far right of beam.") 

