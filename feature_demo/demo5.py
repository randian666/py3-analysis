#!/usr/bin/env python3
# coding:utf-8

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston
'''
数据集的划分：
训练集数据：用于训练，构建模型
测试集数据：在模型检验时使用，用于评估模型是否有效

sklearn.datasets获取流行数据集
datasets.load_*() 获取小规模数据集，数据包含在datasets里

datasets.fetch_*(data_home=None) 获取大规模数据集，需要从网络上下载函数的第一个参数
是data_home，表示数据集下载的目录，第二个参数subset：有'train'或者'test'、'all'可选。

返回的数据类型有：
data:特征数据数组
target:标签数组
desc：数据描述
feature_names:特征名
target_names:标签名
'''

def get_load_iris():
    iris_dataset=load_iris();
    print("获取特征值")
    print(iris_dataset['data'])
    print(iris_dataset['feature_names'])

    print("获取目标值")
    print(iris_dataset['target'])
    print(iris_dataset['target_names'])

    #返回随机的训练集、测试集，test_size表示测试集的百分比
    x_train,x_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],test_size=0.25)
    print("训练集特征值和目标值")
    print(x_train)
    print(y_train)

    print("测试集特征值和目标值")
    print(x_test)
    print(y_test)
'''
获取大数据集
'''
def get_load_20newsgroups():
    news=fetch_20newsgroups(subset='all')
    print(news.data)

'''
获取回归数据集，目标值是连续性的值
'''
def get_load_boston():
    lb=load_boston()
    print("获取特征值")
    print(lb['data'])
    print(lb['feature_names'])

    print("获取目标值")
    print(lb['target'])
    print(lb.DESCR)
if __name__ == '__main__':
    get_load_iris()






