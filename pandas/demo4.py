#!/usr/bin/env python3

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
print('--------------------汇总和计算描述统计----------------------------')
df=DataFrame([[1.4,np.nan],[-1.4,-4.5],[np.nan,np.nan],[0.15,-1.3]],index=list('abcd'),columns=['one','two'])
print(df)
# print(df.sum()) #根据列进行统计
# print(df.sum(axis=1,skipna=False)) #根据行进行统计  skipna排除缺失值，axis轴，行用0 列用1
# print(df.mean())  #平均值

# print(df.idxmax()) #返回最大值的索引
# print(df.describe()) #汇总统计
# df=DataFrame(np.arange(10).reshape(2,5))
# print(df.pct_change()) #相邻两个数字之间的变化率


# obj=Series(['a','b']*4)
# print(obj)
# print(obj.describe())


y_pred = np.where(df > 0.5, 1, 0)
print(y_pred)
