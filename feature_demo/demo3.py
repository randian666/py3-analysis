#!/usr/bin/env python3
# coding:utf-8

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np
'''
数据特征预处理
通过特定的统计方法将数据转换成算法要求的数据
1、归一化
2、标准化
'''


'''
归一化处理
公式:X'=(x-min)/(max-min)  根据范围计算公式： X''=X'*(mx-mi)+mi
特定：通过对原始数据进行变换把数据映射到(默认为[0,1])之间
总结：注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所有这种方法鲁棒性（稳定性）较差，只适合传统精确小数据场景。
目的：使得某一个特征对最终结果不会造成更大的影响。
'''
def mm():
    mm=MinMaxScaler(feature_range=(0,1))
    param = np.array([[90, 2, 10, 40], [60, 4, 15, 45], [75000, 3, 13, 46]])
    # 异常数据演示
    # param = np.array([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46],[75000, 3, 13, 46]])
    data=mm.fit_transform(param)
    print(data)
    print(type(data))

'''
标准化处理
公式：x' =(x - 𝜇)/𝜎  标准化数据通过减去均值然后除以方差（或标准差）
𝜇为平均值，𝜎=sqrt(((x-𝜇)^2 +(x2-𝜇)^2 +......(xn-𝜇)^2)/n)。
# 标准化数据，保证每个维度的特征数据方差为1，均值为0，使得预测结果不会被某些维度过大的特征值而主导
总结：在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景
'''
def stand():
    stand=StandardScaler()
    param=np.array([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    data = stand.fit_transform(param)
    print(data)
    print(type(data))

'''
缺失值处理
缺失值只能是NaN。处理之前需要先把缺失数据替换成NaN。
'''
def im():
   #按列的平均值进行处理
   im= SimpleImputer(missing_values=np.nan,strategy='mean')
   param = np.array([[1,2],[np.nan,3],[7,6]])
   data=im.fit_transform(param)
   print(data)
if __name__ == '__main__':
    im()