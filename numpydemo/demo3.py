#!/usr/bin/env python3

import numpy as np
from numpy.random import randn

arr=np.arange(10)

print(arr)
print(np.sqrt(arr)) #元素级平方根
print(np.exp(arr)) #元素级指数
print(np.square(arr)) #元素级的平方
print(np.ceil(arr))#计算元素级的ceiling值，大于等于改值的的最小整数
print(np.add(arr,arr)) #多个数组元素级相加
print(np.add(arr,arr)) #多个数组元素级相减

arr1=randn(8)
arr2=randn(8)
print(arr1)
print(arr2)
print(np.maximum(arr1,arr2)) #元素级最大值
print(np.modf(arr1))  #将数组的小数和整数部分分别返回
print(np.less(arr1,arr2))
points=np.arange(-5,5,1)
# print(points)
#
# print(np.meshgrid(points,points))
#根据cond中的值选取xarr和yarr的值，cond中的值为True时选取xarr的值否则从yarr中选取
xarr=randn(4)
yarr=randn(4)
cond=np.array([True,False,True,False])
print(xarr)
print(yarr)
print(np.where(cond,xarr,yarr))

arr=randn(4,4)
print(arr)
print(np.where(arr>0,2,-2))#将数组中的正值替换2其他的替换成-2
print(np.where(arr>0,2,arr))#将数组中的正值替换2
print(np.where(arr<0,1,np.where(arr>1,100,200)))#嵌套where


#统计
arr=np.array([[1,2,9],[0,5,6],[2,8,6]])
print(arr.sum()) #所有元素累加
print(arr.mean())  #平均值
print(arr.sum(axis=0))  #根据列求和
print(arr.sum(axis=1))  #根据行求和
print(arr.max(axis=1))
print('------------')
print(arr.max(0))
print(arr.min(0))

# arr=randn(100);
# print((arr>0).sum())  #大于0的数值相加
#
# print(arr.sort())  #排序
# print(arr.argsort()) #返回从小到大的索引值
# print(np.unique(arr)) #返回数组唯一值




