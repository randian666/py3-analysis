#!/usr/bin/env python3

import numpy as np
from numpy.random import randn
import random
arr=np.array([[1,2,3],[4,5,6]])
xarr=np.arange(10)
np.save('some_arr.npy',arr) #数组以未压缩的原始二进制保存在磁盘上，
print(np.load('some_arr.npy')) #读取磁盘数组
np.savez('arr_file.npz',a=arr,b=xarr)  #保存多个文件到磁盘
load_arr=np.load('arr_file.npz')
print(load_arr['a'])

np.savetxt('array_txt.txt',arr,delimiter=',')  #数组存放到txt文件中
arr_txt=np.loadtxt('array_txt.txt',delimiter=',')
print(arr_txt)

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[1,2],[4,5],[2,2]])
print(x.dot(y))
print(np.diag(x))
print(np.trace(x))

print(np.random.randint(100,size=100))

position=0
walk=[position]
steps=1000;
for i in range(steps):
    step=1 if np.random.randint(0,1) else -1
    position +=step;
    walk.append(position)
print(walk)

draws=np.random.randint(0,2,size=steps);
ss=np.where(draws>0,1,-1)
print(ss)
print('##############################')
print(ss.cumsum())
walks=ss.cumsum()
print(walks) #返回两两求和的数组，然后与下一个元素求和的数组
print(walks.max())
print(walks.min())
