#!/usr/bin/env python3
# coding:utf-8

from sklearn.preprocessing import MinMaxScaler

'''
数据特征预处理
1、归一化
2、标准化
'''


'''
归一化处理
公式:X'=(x-min)/(max-min) X''=X'*(mx-mi)+mi
特定:通过对原始数据进行变换把数据映射到(默认为[0,1])之间
总结:注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所有这种方法鲁棒性较差，只适合传统精确小数据场景。
'''
def mm():
    mm=MinMaxScaler(feature_range=(2,3))
    data=mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)
    print(type(data))

if __name__ == '__main__':
    mm()