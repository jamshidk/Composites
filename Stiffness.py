# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:49:09 2018

@author: jamshidkavosi
"""
import numpy as np

def A_Stiffness(myList):
    for i in range(len(myList)):
        PLY1[i]=Ply(myList[i], E1, E2, G12, Nu12, t)
        