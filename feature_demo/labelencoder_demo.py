#!/usr/bin/env python3
# coding:utf-8

# 简单来说 LabelEncoder 是对不连续的数字或者文本进行编号
# sklearn.preprocessing.LabelEncoder()：标准化标签，将标签值统一转换成range(标签值个数-1)范围内

from numpy import array
from numpy import argmax

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
arr_data=array(data)

 #标准化标签，将标签值统一转换成range(标签值个数-1)范围内
le=LabelEncoder()
label_data=le.fit_transform(arr_data)
print(label_data)


#将离散型特征使用one-hot编码，会让特征之间的距离计算更加合理。离散特征进行one-hot编码后，编码后的特征，其实每一维度的特征都可以看做是连续的特征。
# 就可以跟对连续型特征的归一化方法一样，对每一维特征进行归一化。
one_data=[["男", 0, 3], ["男", 1, 0], ["中性", 2, 1], ["女", 0, 2]]
onehot_encoder = OneHotEncoder(sparse=False)
onehot_data = onehot_encoder.fit_transform(one_data)
print(onehot_data)
#查看独热编码每一列代表的意义
print(onehot_encoder.get_feature_names())






