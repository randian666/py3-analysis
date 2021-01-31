#!/usr/bin/env python3
'''
相关性系数（pearson、spearman、kendall，pointbiserialr）
检查两个变量之间变化趋势的方向以及程度，值范围-1到+1，0表示两个变量不相关，正值表示正相关，负值表示负相关，值越大相关性越强。
'''
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

a = np.arange(1,10).reshape(3,3)
data = DataFrame(a,index=["a","b","c"],columns=["one","two","three"])
print(data.info())
print("-----------------------------------------------")
print(data)
print("-----------------------------------------------")
#返回一个相关系数矩阵
print(data.one.corr(data.two))
