#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

print('-----------------Series排名排序----------------------')
obj=Series(range(4),index=['a','c','b','d'])
print(obj.sort_index()) #Series根据索引排序
print(obj.sort_values()) #Series根据值排序
obj=Series([7,-5,7,3,4,2])
print(obj.rank())#rank：排名值 method：排名时用于破坏平级关系的选项
print(obj.rank(method='first'))
print(obj.rank(method='max'))
print(obj.rank(method='min'))
#first按值在原始数据中出现顺序分配排名
#max使用整个分组的最大排名
#min使用整个分组的最小排名
#average 默认：在相等分组中，为各个值分配平均排名
print('-----------------Dataframe排名排序----------------------')
frame=DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
print(frame)
print(frame.sort_index()) #根据行索引排序
print(frame.sort_index(axis=1)) #根据列索引排序
print(frame.sort_index(axis=1,ascending=False)) #倒序
df=DataFrame({'a':[4,7,-3,2],'b':[0,1,0,1]})
print(df)
print(df.sort_values(by=['a'],ascending=False)) #根据列值进行排序
print(df.rank(axis=1))

