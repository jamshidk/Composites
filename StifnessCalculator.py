# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:07:32 2018

@author: jamshidkavosi
"""
import numpy as np

from numpy import cos, inf, zeros, array, exp, conj, nan, isnan, pi, sin
#import Scipy as sp

from Ply import *
from A_calc import *
from B_calc import *
from D_calc import *
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


sequence=[-45,45]
E1=[19.981e9,19.981e9]
E2=[11.389e9,11.389e9]
G12=[3.789e9,3.789e9]
Nu12=[0.274,0.274]
t=[0.635,0.635]

##################################
z=[0]*(len(sequence)+1)
z_bar=[0]*len(sequence)
thickness=0
####################################
#ABD=np.zeros((6,6), dtype=float)
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
      

#ABD= np.concatenate(A_calc(sequence,E1,E2,G12,Nu12,t,z_bar), B_calc(sequence,E1,E2,G12,Nu12,t,z_bar)) 
#print(ABD)
##PLY1.ABD_calculator()




#print(A)