#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
'''
Series是一种类似一维数组的对象，它是由一组数据（Numpy数据类型）以及一组与之相关的数据标签组成
'''
print('---------------------------------------')
obj=Series([4,7,8,-9])
print(obj)
print('values:',obj.values)#数组
print('index:',obj.index)  #索引对象
print('---------------------------------------')
obj2=Series([1,2,3,-4],index=['a','b','c','d'])
print(obj2)
print(obj2.index)
print(obj2['a']) #选取Series中的单个
print(obj2[['a','b','c']]) #获取Series一组值
print('b' in obj2) #索引值到数据值的映射
print('---------------------------------------')
#NumPy数组运算
print(obj2[obj2>2])
print(obj2*2)
print(np.square(obj2))
print(np.where(obj2>2,444,obj2))
print('---------------------------------------')
#Python字典来创建Series 索引就是字典的键
sdata={'Joe':100,'Bob':200,'Utah':1000}
print(Series(sdata))
states=['Joe','Bob']
obj4=Series(sdata,index=states) #sdata中跟states索引相匹配的值找出来放到相应的位置
print(obj4)
print(pd.isnull(obj4)) #检测缺失数据
print(obj4.isnull())
obj4.name='population'
obj4.index.name='state'
obj4.index=['Bobs','Joes']  #修改索引
print(obj4)
print('---------------------------------------')
sdata1={'Joe':101,'Bob':200}
obj5=Series(sdata1,index=states)
obj6=Series({'Joe':100,'Bob':200,'Demo':300})
obje7=obj5+obj6
print(obj5+obj6) #算数运算中会自动对齐不同索引的数据
print(obje7.isnull())
print(pd.isnull(obje7))
for v in obje7.values:
    print(v)
print('---------------------------------------')
print('---------------------------------------')
#索引修改
obj=Series([4,5,1,3],index=['a','b','c','d'])
print(obj)
obj2=obj.reindex(['a','b','c','d','e'],fill_value=0.0) #不存的索引就引入缺失或者fill_value
print(obj2)