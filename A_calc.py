# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:49:09 2018

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
        
        