# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:56:47 2018

@author: jamshidkavosi
"""

import numpy as np
from ply import *



def Stress(ABD,strain):
    return ABD*strain

def Strain(iABD,stress):
    return iABD*stress