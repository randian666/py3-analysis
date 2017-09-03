#!/usr/bin/env python3

import numpy as np
'''
ndarray是一个通用的同构数据多维容器
'''
data=[1,2.2,2,3,4]
npdata=np.array(data,dtype=np.float64) #np.array创建ndarray数组 dtype为数组的数据类型
print(npdata)
print(npdata.shape) #返回数组维度大小的元组
print(npdata.dtype) #返回数组数据类型

data1=[[1,2,3,4,5],[2,3,4,5,6]]
npdata1=np.array(data1)
print(type(npdata1))
print(npdata1)
print(npdata1.shape)
print(npdata1.dtype)
#除了np.array之外，还有zeros和ones分别可以创建指定长度或形状的全0或全1数组

print(np.zeros((2,2,10)))
print(np.ones(10))
print(np.empty((2,3,2)))


#arange是内置函数range的数组版 默认数据类型是float64
print(np.arange(10))
#创建一个正方的N*N单位矩阵 对角线为1
print(np.eye(5))
print(np.identity(4))

#数据类型转换
array=np.array([1,2,3,4,5])
print(array.dtype)
array_two=array.astype(np.string_);
print(array_two.dtype)

#如果将浮点类型换成整数，则小数部分将会被截断
array=np.array([1,1,2.1,3.3])
print(array.dtype)
array_two=array.astype(np.int64)
print(array_two)

#字符串数组转换成数字
numeric_strings=np.array(['1.1','1.2','1.3'],dtype=np.string_)
numeric_int=numeric_strings.astype(np.float64)
print(numeric_int)


