# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:07:32 2018

@author: jamshidkavosi
"""
import numpy as np

from numpy import cos, inf, zeros, array, exp, conj, nan, isnan, pi, sin
#import Scipy as sp

from Ply import *
from ABD_calculator import *

from StressStrain import *

# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox


#def A_calc(myList):
 #  for i in range(len(myList)):
   #    PLY=Ply(myList[i], E1, E2, G12, Nu12, t)
   #    A=+ PLY.ABDcalculator()
        

top = Tk()
top.geometry("200x200")
#def hello():
 #  messagebox.showinfo("Say Hello", "Hello Jamshid")

#B1 = Button(top, text = "Say Hello", command = hello)
#B1.place(x = 100,y = 100)

#top.mainloop()


sequence=[0,90,-90,-90,90,0]
E1=[20e9,20e9,20e9,20e9,20e9,20e9]
E2=[4e9,4e9,4e9,4e9,4e9,4e9]
G12=[6.89e9,6.89e9,6.89e9,6.89e9,6.89e9,6.89e9]
Nu12=[0.25,0.25,0.25,0.25,0.25,0.25]
t=[0.5,0.5,0.5,0.5,0.5,0.5]

##################################
z=[0]*(len(sequence)+1)
z_bar=[0]*len(sequence)
thickness=0
####################################
##state of stress and strain##
strain=[[0],[90],[-90],[-90],[90],[0]]
stress=[[0],[0],[0],[1000],[0],[0]]

####################################

ABD=np.zeros((6,6), dtype=float)
#print(ABD)
for i in range(len(sequence)):
    thickness=thickness+t[i]
    
z[0]=-thickness/2

for j in range(1,len(sequence)+1):
    z[j]=z[j-1]+t[j-1]
    
for q in range(len(sequence)):
    z_bar[q]=(z[q]+z[q+1])/2
    
    
#print(z)
#print(z_bar)

A=A_calc(sequence,E1,E2,G12,Nu12,t,z_bar) 
B=B_calc(sequence,E1,E2,G12,Nu12,t,z_bar)
D=D_calc(sequence,E1,E2,G12,Nu12,t,z_bar)
print('A=',A)
print('B=',B)
print('D=',D)
      


AB= np.concatenate((A, B), axis=1) 
BD= np.concatenate((B, D), axis=1)
ABD=np.concatenate((AB, BD), axis=0)  
iABD=np.linalg.inv(ABD)

print(Strain(iABD, stress))
print('iABD=', iABD)
##PLY1.ABD_calculator()




#print(A)