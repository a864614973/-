# import matplotlib.pyplot as plt
import math
import sympy
import numpy as np
# from scipy.optimize import fsolve
from sympy import *
from scipy.optimize import root
from scipy.optimize import fsolve,leastsq
np.set_printoptions(suppress=True)
# y(厚度，里程，寿命)
# y=[[1,1,1,480,480,480,600],[3.248,2.776,3.248,3.2,2.8,2.6,2.51],[16.9,16.9,16.9,10.6,12.2,8.0,8.1]]
y=[[1,1,1,480,480,480,600],[3.248,2.776,3.248,3.2,2.8,2.6,2.51],[0,0,0,6.3,4.7,8.9,8.8]]
# y=[[1,1,1,480,480,600],[3.248,2.776,3.248,3.2,2.8,2.51],[0,0,0,6.3,4.7,8.8]]
# y=[[480,480,480,600],
#    [3.2,2.8,2.6,2.51],
# [6.3,4.7,8.9,8.8]]

def MaxMinNormalization(x,Max,Min):
    x = (Max-x)/(Max-Min)
    return x
for i in range(len(y)-1):
    y[i]=(MaxMinNormalization(y[i],np.array(y[i]).max(),np.array(y[i]).min())).tolist()
for i in range(len(y[0])):
    y[0][i]=1-y[0][i]
for i in range(len(y)):
    for j in range(len(y[i])):
        if y[i][j]==0:
            y[i][j]=0.001
def solve_function(unsolved_value):
    F = [];
    w1,w2,b=unsolved_value[0],unsolved_value[1],unsolved_value[2]
    for i in range(3,len(y[2])):
        f=(0.5*math.log(w1*(y[0][i]**2)+w2*(y[1][i]**2))-0.5*math.log(w1*(y[0][0]**2)+w2*(y[1][0]**2)))/y[2][i]-b
        F.append(f)
    return F


x = Symbol('x')
y=  Symbol('y')
z=  Symbol('z')

# F=[(0.5*math.log(w1*(0.79967**2)+w2*(0.60704607**2))-0.5*math.log(w1*(0.001**2)+w2*(0.001**2)))/4.7-b,
#    (0.5*math.log(w1*(0.79967**2)+w2*(0.8780488**2))-0.5*math.log(w1*(0.001**2)+w2*(0.001**2)))/8.9-b,
#    (0.5*math.log(w1*(1**2)+w2*(1**2))-0.5*math.log(w1*(0.001**2)+w2*(0.001**2)))/8.8-b]
def f1(x,y,z):
    return [(0.5*sympy.log(x*(0.79967**2)+y*(0.60704607**2))-0.5*sympy.log(x*(0.001**2)+y*(0.001**2)))/4.7-z,(0.5*sympy.log(x*(0.79967**2)+y*(0.8780488**2))-0.5*sympy.log(x*(0.001**2)+y*(0.001**2)))/8.9-z,(0.5*sympy.log(x*(1**2)+y*(1**2))-0.5*sympy.log(x*(0.001**2)+y*(0.001**2)))/8.8-z]



solved_value=solve(solve_function([x,y,z]), [50,50,5])
print(solved_value)