# ENG-104-EC-Project
import numpy as np

def f_AOT(F_B1,F_B2,r_B,L_BC,r,G): 
    #F_B1,F_B2,F_C1,F_C2 Forces at BC [KN]
    #r_B,r_C Radius pulley [mm]
    #r radius of shaft [mm]
    #L_BC length of Shaft from B to C [m]
    #G shear modulus [GPa]
    T_B=(F_B1-F_B2)*r_B #torque at B [NM]
    J=np.pi/32*(r*2/1000)**4
     ## Angle of twist
    Theta=T_B*L_BC/((G*(10**9))*J)
    return print(Theta) #[MPa],[rad]


def f_mAxShear(F_B1,F_B2,F_C1,F_C2,r_B,r_C,r):

    T_B=(F_B1-F_B2)*r_B #torque at B [NM]
    #T_C=(F_C1-F_C2)*r_C #torque at C [NM]
    J=np.pi/32*(r*2/1000)**4
    Tau=(T_B*r/1000)/J
    return print(Tau/(10**6))


f_AOT(6,2,150,1,40,80)
f_mAxShear(6,2,10,4,150,100,40)
 ##HW 4 problem 3
