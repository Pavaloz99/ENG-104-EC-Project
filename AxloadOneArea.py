# For Compatibility = 0
# For Constant area

import numpy as np

print("What is the compatibility condition for this problem? (meters)")
delta = float(input())

print("What is the number of external axial loadings?")
NumbersF = int(input())

print("State the forces from left to right as shown in the problem")

g = np.empty(NumbersF)
for i in range(NumbersF):
    g[i] = float(input())
    ForceArray = g

print("Distance from leftmost fixed end to each applied axial load in order of stated forces (in meters)")

h = np.empty(NumbersF)
for i in range(NumbersF):
    h[i] = float(input())
    Dleft = h

print("What is the length of the beam?")
Dfull = float(input())

Dright = Dfull-Dleft[0:NumbersF]


if delta == 0:
    if NumbersF == 1: # 1 force
        print("Axial Force P = " + str(ForceArray) + " newtons")
        print()
        print("Distance from leftmost fixed end to applied axial load (in meters)")
        print("L1 = "+ str(Dleft[0]) + " meters")
        print()
        print("Distance from rightmost fixed end to applied axial load (in meters)")
        print("L2 = " + str(Dfull-Dleft[0]) + " meters")
        print()
        print("Calculating...")
        print()

        P = ForceArray[0]
        Lab = Dfull
        Lac = Dleft[0]
        Lbc = Dfull-Dleft[0]
        Fa = -Lbc*P/Lab
        Fb = -Lac*P/Lab
        print("Fa = " + str(Fa) + " Newtons")
        print("Fb = " + str(Fb) + " Newtons")
        print("*If F is positive, reaction points right. If F is negative, reaction points left. (For vertical beams, negative forces point up)")
        print("Fa located at far left of beam and Fb located at far right of beam. (For vertical beams, Fa is top reaction and Fb is bottom reaction)") 

    if NumbersF > 1:
        print("Axial Forces P = " + str(ForceArray) + " newtons")
        print()
        print("Distances from leftmost fixed end to each applied axial load (in meters)")
        print("L1 = "+ str(Dleft[0:NumbersF]) + " meters")
        print("Distance from rightmost fixed end to applied axial load (in meters)")
        print("L2 = " + str(Dfull-Dleft[0:NumbersF]) + " meters")
        print()
        print("Calculating...")
        print()

        c = NumbersF + 1 # Amount of segments
        j = NumbersF - 1 # Last array value index
        LengthSeg = np.empty(c)
        for i in range(c): # Find lengths of each segment and put into array
            x = i - 1
            if i == 0:
                LengthSeg[i] = Dleft[0]
            elif i != 0 and i < NumbersF:
                LengthSeg[i] = Dleft[i] - Dleft[x]
            elif i == NumbersF:
                LengthSeg[i] = Dfull - Dleft[j]

        Fsum = np.empty(NumbersF) # partial sum of internal forces for each relative displacement
        for w in range(NumbersF): # To fill Fsum array
            f1w = ForceArray[w]

            if w == 0:
                fs = f1w
            else:
                fs = y

            Fsum[w] = fs

            if w != NumbersF-1:
                y = fs + ForceArray[(w+1)]  

        # Calculate Fa and Fb
        Lsum = sum(LengthSeg)
        FaA = sum(Fsum * LengthSeg[1:c])
        Fa = FaA / Lsum 
        Fb = Fa - sum(ForceArray)      
        print("Reaction force Fa = " + str(Fa) + " (newtons)")
        print("if Fa is positive, Fa points to the left (Fa = left support rxn)") 
        print()
        print("Reaction force Fb = " + str(Fb) + " (newtons)")
        print("if Fb is positive, Fb points to the right (Fb = right support rxn)")
            



                








        

        

