import numpy as np
import matplotlib.pyplot as plt

##相对于不是很大的数据来说，正规方程相对于梯度下降运算更加的简便

# x=[[400],[450],[484],[500],[510],[525],[540],[549],[558],[590],[610],[640],[680],[750],[900]]
# y=[[80],[89],[92],[102],[121],[160],[180],[189],[199],[203],[247],[250],[259],[289],[356]]
# plt.plot(x,y,'ks')
# end=[[0],[0]]
# for i in range(len(x)):
#     x[i].insert(0,1)
# x=np.mat(x)#转成矩阵
# y=np.mat(y)
# end=np.mat([0,0])
# end=end.T#矩阵转逆
# end=(x.T*x).I*x.T*y
# end=end.getA().tolist()#矩阵转成列表
# print(end)
# X=[400,900]
# Y=[]
# Y.append(end[0][0]+end[1][0]*X[0])
# Y.append(end[0][0]+end[1][0]*X[1])
# plt.plot(X,Y,'g-')
# plt.show()
