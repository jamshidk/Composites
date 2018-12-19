# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:20:30 2018

@author: jamshidkavosi
"""

import numpy as np
from Ply import *


def A_calc(sequence,E1,E2,G12,Nu12,t,z_bar):
    
    A=matrix([[0,0,0],
              [0,0,0],
              [0,0,0]])
    
    for i in range(len(sequence)):
        PLY=Ply(sequence[i], E1[i], E2[i], G12[i], Nu12[i], t[i], z_bar[i])
        A= A+ PLY.A_calculator()
        
    return A



def B_calc(sequence,E1,E2,G12,Nu12,t,z_bar):
    
    B=matrix([[0,0,0],
              [0,0,0],
              [0,0,0]])
    
    for i in range(len(sequence)):
        PLY=Ply(sequence[i], E1[i], E2[i], G12[i], Nu12[i], t[i], z_bar[i])
        B= B+ PLY.B_calculator()
        
    return B


def D_calc(sequence,E1,E2,G12,Nu12,t,z_bar):
    
    D=matrix([[0,0,0],
              [0,0,0],
              [0,0,0]])
    
    for i in range(len(sequence)):
        PLY=Ply(sequence[i], E1[i], E2[i], G12[i], Nu12[i], t[i], z_bar[i])
        D= D+ PLY.D_calculator()
        
    return D