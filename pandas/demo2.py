#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
print('---------------------------------------')
#索引修改
obj=Series([4,5,1,3],index=['a','b','c','d'])
print(obj)
obj2=obj.reindex(['a','b','c','d','e'],fill_value=0.0) #不存的索引就引入缺失或者fill_value
print(obj2)

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
print(data[:2])
print(data[data['a1']>4])
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

#Dataframe与Series之间的运算
arr=DataFrame(np.arange(15).reshape(5,3),columns=list('abc'),index=['ShangHai','BeiJing','Changsha','Hangzhou','Fujian'])
print(arr[])



