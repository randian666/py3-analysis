#!/usr/bin/env python3

import numpy as np
from numpy.random import randn
'''
numpy数据计算
不用编写循环既可对数据执行批量运算，任何算数运算都会将运算应用到元素级
'''

arry=np.array([[1,2,3,4,4],[2,2,1,3,5]])
print(arry* arry)
print(arry+arry)
print(arry*0.5)

#数组切片
print('~~~~~~~~~~数组切片~~~~~~~~~~~~~~~~~~')
arrys=np.arange(10)
print(arrys)
print(arrys[5])
print(arrys[0:5])
print(arrys[5].copy())

#多维数组访问
print('~~~~~~~~~~多维数组访问~~~~~~~~~~~~~~~~~~')
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[0][2])
print(arr2d[0][0:2])
print(arr2d[0,2])
print(arr2d[0,0:2])

arr2d[0]=99
print(arr2d)
#多维数组切片
print("~~~~~~~~~~~~~~~~~~多维数组切片~~~~~~~~~~~~~~")
arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d[0])
print(arr3d[1,0])
print(arr3d[:2,1:])
print(arr3d[:,1:])

#布尔型索引 比较运算将会产生一个布尔型的数组
names=np.array(['Bob','Joe','Will','Bob','Will'])
print(names=='Bob')
print(names!='Bob')
print((names=='Bob') | (names=='Will'))  #使用&（和）|（或）算术运算符选取多个布尔条件
print(names[0:2])
data=randn(5,4)
print(data)
print(data[names=='Bob',:]) #可以用于数组索引，布尔数组的长度必须跟被索引的轴长度一致。查找为True的行

