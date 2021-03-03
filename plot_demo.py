from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
import sympy

fig = plt.figure()
ax = Axes3D(fig)
x=np.arange(0,1,0.01)
y=np.arange(0,1,0.01)
X, Y = np.meshgrid(x, y)#网格的创建，这个是关键
# # 我的程序
# solved=[[2.011815422501494e+02, 8.036073146926254e+03,    0.784972190793425]]
# X = np.linspace(0, 10, 1000)
# Z=16.9-8.8*X
# #解决中文显示问题
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.xlabel('x')
# ax.set_xlabel('归一化后的里程数')
# plt.ylabel('y')
# ax.set_ylabel('归一化后的绝缘平均厚度')
# ax.set_zlabel('电缆剩余寿命（年）')
# ax.plot_surface(X, (1-Y), Z, rstride=1, cstride=2, cmap='coolwarm')
# # ax.plot_surface(X,  Z, rstride=1, cstride=2, cmap='coolwarm')
# plt.show()


# 周利辉图   X——A   Y——M
# # 车端过桥线位置
# Z=5.85*10**4+(3.239*10**5)*X+(-7.816*10**4)*Y+(-2.423*10**5)*X**2+(1.414*10**4)*X*Y
# #运行配电盘和服务配电盘之间的跨接线（走顶棚）
Z=9.662*10**4-2.479*10**4*X-2.917*10**4*Y
# #影视柜到客室电视位置
# Z=2.06*10**5+5.466*10**4*X+4.161*10**4*Y
# Z=np.maximum(Z,0)
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('x')
ax.set_xlabel('归一化后的绝缘平均厚度')
plt.ylabel('y')
ax.set_ylabel('归一化后的里程数')
ax.set_zlabel('电缆剩余寿命（小时）')

plt.title('影视柜到客室电视电缆寿命曲线')
ax.plot_surface(X, Y, Z, rstride=1, cstride=2, cmap='coolwarm')
plt.show()