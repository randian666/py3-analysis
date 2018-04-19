#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
'''
DataFrame是一个表格型的数据结构，它包含一组有序的列，每列可以是不同的值类型。DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典。
'''
data={"state":['a','b','c','d'],"year":['2010','2011','2012','2013']}
data_frame=DataFrame(data)
print(data_frame)
print('---------------------------------------')
frame=DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['Ohio','Texas','China'])
print(frame)
print(frame.reindex(['a','b','c','d'],fill_value=-1))
print(frame.reindex(columns=['Ohio','Utah','China']))
#删除
print('---------------------------------------')
new_obj=frame.drop(['a','c']) #根据行索引删除一行数据
print(new_obj)
print(frame.drop('Ohio',axis=1)) #根据列索引删除一列数据
#索引、选取、过滤
print('---------------------------------------')
obj=Series(np.arange(4),index=['a','b','c','d'])
print(obj['a':'c']) #根据行索引切片，与普通的python切片不同的时候末端是包含的
obj['a':'c']=5
print(obj)
print('---------------------------------------')
data=DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],columns=['a1','b1','c1','d1'])
print(data)
print(data[:2]) #通过切片获取数据
print(data[data['a1']>4])  #通过bool索引获取数据
print(data['a1'])
print(data.ix['a',['a1','b1']]) #获取第一个参数是行索引，第二个是列索引的范围
print(data.ix[data.a1>4,:3])
print(data.ix['a','a1'])
#算数运算和数据对齐
print('---------------------------------------')

d1=DataFrame(np.arange(15).reshape(3,5),index=list('abc'))
d2=DataFrame(np.arange(20).reshape(4,5),index=list('abcd'))
print(d1+d2)  #相加会自动在不重叠的索引处引入NaN，也可以设置默认缺失值
print(d1.add(d2,fill_value=0)) #加
print(d1.sub(d2,fill_value=0)) #减
print(d1.div(d2,fill_value=0)) #除
print(d1.mul(d2,fill_value=0)) #乘
print('-----------------Dataframe与Series之间的运算----------------------')
#Dataframe与Series之间的运算
arr=DataFrame(np.arange(15).reshape(5,3),columns=list('abc'),index=['ShangHai','BeiJing','Changsha','Hangzhou','Fujian'])
series=arr.ix[0]  #获取第一行数据
print(arr)
print(series)

print(arr-series)  #默认情况下，DF和Series之间的算术运算会将Series的索引匹配到DF的列，然后向下广播
print(arr.sub(arr['a'],axis=0)) #在列上进行广播
print('-----------------Dataframe函数应用和映射----------------------')
frame=DataFrame(np.random.randn(4,3),columns=list('bde'),index=['ShangHai','BeiJing','Changsha','Hangzhou'])
print(frame)
f=lambda x:x.max()-x.min();
print(frame.apply(f)) #在列上进行广播 将函数应用到由各列或各行所形成的一堆数组上。使用apply方法
print(frame.apply(f,axis=1)) #在行上进行广播
print(np.abs(frame))
def f(x):
    return Series([x.max(),x.min()],index=['max','min']) #列的最大值\最小值
print(frame.apply(f))

format=lambda x:'%.2f'%x;#得到各个元素中的浮点值的格式化字符串
print(frame.applymap(format)) #元素级的Python函数可以用

