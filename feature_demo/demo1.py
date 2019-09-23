#!/usr/bin/env python3
#coding:utf-8

from sklearn.feature_extraction import DictVectorizer

'''
字典数据抽取：把字典中的一些类别数据，分别进行转换成特征（one-hot编码）。
'''
def dictvec():
    #实例化DictVectorizer
    #sparse=True 输出sparse矩阵：节约内存，方便读取处理。
    #sparse=False 输出ndarray 二维数组
    dict=DictVectorizer(sparse=False)
    #调用fit_transform进行特征转化
    data=dict.fit_transform([{'city':'上海','etmperature':100},{'city':'北京','etmperature':70},{'city':'成都','etmperature':30}])
    print(data)
    print(type(data))
    #输出类别名称
    print(dict.get_feature_names())

if __name__ == '__main__':
    dictvec()