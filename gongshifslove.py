import math
from scipy.optimize import fsolve,leastsq
import numpy as np
import sympy


np.set_printoptions(suppress=True)
# y(厚度，里程，寿命)
# y=[[1,1,1,480,480,480,600],[3.248,2.776,3.248,3.2,2.8,2.6,2.51],[16.9,16.9,16.9,10.6,12.2,8.0,8.1]]
y=[[1,1,1,480,480,480,600],[3.248,2.776,3.248,3.2,2.8,2.6,2.51],[0,0,0,6.3,4.7,8.9,8.8]]

# 归一化
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
    for i in range(4,len(y[2])):
        f=((0.5*sympy.log(w1*(y[0][i]**2)+w2*(y[1][i]**2))-0.5*sympy.log(w1*(y[0][0]**2)+w2*(y[1][0]**2)))/y[2][i])-b
        F.append(f)
    return F
print(y)
# print(solve_function([1,1,1]))
solved=fsolve(solve_function,[100,100,1])
print(solved)
print("===================")
print("求解函数名称:",leastsq.__name__)
print("解：",solved[0])
print(y)
# solved=[[5.281454775753919e+03, 9.181849677272849e+03,    0.784971757820483]]
solved=[[2.011815422501494e+02, 8.036073146926254e+03,    0.784972190793425]]
y_pre=[]
for i in range(3,len(y[2])):
    a=(0.5*math.log(solved[0][0]*(y[0][i]**2)+solved[0][1]*(y[1][i]**2))-0.5*math.log(solved[0][0]*(y[0][0]**2)+solved[0][1]*(y[1][0]**2)))/solved[0][2]
    y_pre.append(a)
print("预测值")
print(y_pre)
print("真实值")
y_real=y[2][3:]
print(y_real)
sum=0
for i in range(len(y_pre)):
    a=(y_pre[i]-y_real[i])**2
    sum+=a
    erro=sum/len(y_pre)

print(erro)

