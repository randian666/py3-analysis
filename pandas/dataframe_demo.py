#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
'''
DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同类型的值。
DataFrame既有行索引也有列索引，可以看做是由Series组成的字典
'''
print('---------------------------------------')
data={'name':['Bob','Zhangsan','LiBai'],
      'age':[11,13,12],
      'score':[100,120,102]}
df1=DataFrame(data);
print(df1)
#如果指定了列序列，就会按照指定的顺序排列
df3=DataFrame(data,columns=['name','age','score'])
print(df3)
#如果传入的列在数据找不到就会生成NaN
df2=DataFrame(data,columns=['name','age','score','addr'],index=['one','two','thrid'])
print(df2)
print('---------------------------------------')
#可以将DataFrame列获取尾一个Series
print(df2['name'])
print(df2.name)
#根据行索引获取一行数据
print(df2.ix['one'].values) #values返回ndarray数组
print(df2)
print('---------------------------------------')
#赋值
df2['score']=np.arange(3)
df2['addr']=np.arange(3)
val=Series(['china','usa'],index=['one','two'])
df2['addr']=val
print(df2)
df2['adult']=df2.age>18
print(df2)
print('---------------------------------------')
#嵌套字典,外层字典的键作为列索引，内层的键作为行索引
pop={'Nevada':{2001:7.4,2002:3.3},'Ohio':{2000:8.3,2001:1.7}}
popdata=DataFrame(pop)
print(popdata)
print(popdata.T) #转置行转列
print('---------------------------------------')
#设置DataFrame的index和name属性
popdata.index.name='year'
popdata.columns.name='state'
print(popdata)
print('Nevada' in popdata.columns) #判断列索引是否存在
print(2001 in popdata.index) #判断行索引是否存在


