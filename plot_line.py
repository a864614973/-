# -*- coding: utf-8 -*- 
import numpy as np


import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.grid()
# x = [1,1,0, 0]
# y = [2.8,4.1,5.1,5.83]
# plt.plot(x, y) #x， y是两个列表
# plt.xlabel("归一化后的里程数")
#
# #Y轴的文字
# plt.ylabel("电缆剩余寿命（年）")
#
# #图表的标题
# plt.title("牵引变压器-牵引变流器电缆寿命曲线")
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
def linear_regression(x, y):
    N = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumx2 = sum(x ** 2)
    sumxy = sum(x * y)
    A = np.mat([[N, sumx], [sumx, sumx2]])
    b = np.array([sumy, sumxy])
    return np.linalg.solve(A, b)

#单臂
#修改数据1：
X1=np.array([1,0])
Y1=np.array([63072,128772])



a0, a1 = linear_regression(X1, Y1)
# 生成拟合直线的绘制点
_X1 = [0, 1]
_Y1 = [a0 + a1 * x for x in _X1]

a0, a1 = linear_regression(X1, Y1)
#显示图像
# plt.plot( X1, Y1, 'ro', linewidth=1)
plt.plot(_X1, _Y1, 'b',linewidth=1,color='C0')

plt.xlabel("归一化后的里程数")
plt.ylabel("电缆剩余寿命（小时）")
plt.title("转向架和车体之间电缆寿命曲线")
plt.legend()
plt.show()