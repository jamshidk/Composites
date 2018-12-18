# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:38:38 2018

@author: jamshidkavosi
"""
import numpy as np
from Ply import *


def D_calc(sequence,E1,E2,G12,Nu12,t,z_bar):
    
    D=matrix([[0,0,0],
              [0,0,0],
              [0,0,0]])
    
    for i in range(len(sequence)):
        PLY=Ply(sequence[i], E1[i], E2[i], G12[i], Nu12[i], t[i], z_bar[i])
        D= D+ PLY.D_calculator()
        
    return D