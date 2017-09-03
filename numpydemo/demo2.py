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
print('----------------------布尔型索引--------------------------')
#布尔型索引 比较运算将会产生一个布尔型的数组
names=np.array(['Bob','Joe','Will','Bob','Will'])
print(names=='Bob')
print(names!='Bob')
print((names=='Bob') | (names=='Will'))  #使用&（和）|（或）算术运算符选取多个布尔条件
print(names[0:2])
data=randn(5,4)
print(data)
print(data[names=='Bob',:]) #可以用于数组索引，布尔数组的长度必须跟被索引的轴长度一致。查找为True的行
data[data<0]=0      #通过布尔数组将data中的所有负值设置为0
print(data)

print('----------------------花式索引--------------------------')
data1=np.empty((8,4));
for n in range(8):
    data1[n]=n
print(data1)
#选取特定行子集，只需要传入一个列表或者ndarray
print(data1[[1,2,3]])
dd=np.arange(32).reshape(8,4)
print(dd)
print(dd[np.ix_([1,5,7,2],[0,3,1,2])]) #ix_将数组转换为一个方形区域的索引器
print(dd[np.ix_([0,1,2],[0,1,2,3])]) #第一个[]是选择行的数组、第二个是列的索引

#数组的轴对换
print('----------------------数组的轴对换--------------------------')
arr=np.arange(12).reshape(3,4)
print(arr)
print(arr.T) #行转列

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.T)
print(np.dot(arr.T,arr));

arr=np.arange(16).reshape(2,2,4)
print(arr)
print(arr.transpose((1,0,2)))
print(arr.swapaxes(1,2)) #多维数组行转列