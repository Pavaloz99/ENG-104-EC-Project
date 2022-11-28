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
  
    Theta=T_B*L_BC/((G*(10**9))*J)
    return Theta #[MPa],[rad]


#HW4 q3 ( Angle of twist function)
