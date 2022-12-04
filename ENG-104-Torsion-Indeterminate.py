# ENG-104-Torsion-Indeterminate

def f_TorsionInd(T_C,T_D,L_BC,L_CD,L_DA): 
    #T_C Torque at C [N*m]
    #T_D Torque at D [N*m]
    #L_BC Length of shaft from B to C [m]
    #L_CD Length of shaft from C to D [m]
    #L_DA Length of shaft from D to A [m]
    T_B = (L_DA*(-T_C-T_D)-L_CD*T_C)/(L_BC+L_CD+L_DA) #Torque at B [N*m]
    T_A = -T_B-T_C-T_D #Torque at A [N*m]
    return print(T_B, T_A, sep=', ')

f_TorsionInd(-800,500,0.2,1.5,0.3)
#Textbook Example 5.8