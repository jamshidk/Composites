# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:06:37 2018

@author: jamshidkavosi
"""
import numpy as np
import math

from numpy import cos, inf, zeros, array, exp, conj, nan, isnan, pi, sin, matrix, square, transpose

class Ply:
    def __init__(self, Angle, E1, E2, G12, Nu12, t, z_bar):
        self.Angle= Angle
        self.E1=E1
        self.E2=E2
        self.G12=G12
        self. Nu12= Nu12
        self.Nu21=(self.E2/self.E1)*self.Nu12
        self.t=t
        self.z_bar=z_bar
        self.Angle= (pi/180)*self.Angle
        
        
        
        
    def Q_calculator(self):
        m= cos(self.Angle)
        n=sin(self.Angle)
        T= matrix([ [square(m), square(n),  2*m*n ],
                         [square(n), square(m), -2*m*n ],
                         [-m*n,         m*n,           square(m)-square(n)]])
    
        S= matrix([ [1/self.E1, -self.Nu21/self.E2,  0 ],
                       [-self.Nu12/self.E1, 1/self.E2, 0 ],
                       [0,         0,           1/self.G12]]);
        Q=np.linalg.inv(S);
        Q_bar= np.linalg.inv(T)*Q*transpose(np.linalg.inv(T));
    
        return Q_bar
    #Angle=input('Please enter the Angle in degree:')
    #E1=input('Please enter the E1 in GPa:')
    #E2=input('Please enter the E2 in GPa:')
    #G12=input('Please enter the G12 in GPa:')
    #Nu12=input('Please enter the Nu12 :')
    #t=input('Please enter the thickness of the ply in mm :')
    

    
    def A_calculator(self):
        A=self.Q_calculator()*self.t
        return A
    
        
    def B_calculator(self):
        B=self.Q_calculator()*self.t*self.z_bar
        return B
        
    def D_calculator(self):
        D=self.Q_calculator()*(self.t*np.square(self.z_bar)+(self.t**3)/12)
        return D