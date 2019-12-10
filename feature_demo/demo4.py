#!/usr/bin/env python3
# coding:utf-8
from sklearn.feature_selection.variance_threshold import VarianceThreshold
from sklearn.decomposition import PCA
'''
数据降维（指的是特征的数量）
降维方式：
1、特征选择
2、主成分分析
'''


'''
特征选择
冗余：部分特征的相关度高，容易消耗计算机性能
噪声：部分特征对预测结果有影响
主要方法：
过滤式（Filter）：VarianceThreshold
嵌入式（Embedded）：正则化、决策树、神经网络等
包裹式（Wrapper）
'''

'''
特征选择-删除低方差的特征
'''
def var():
    var=VarianceThreshold(threshold=0)
    data=var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)
    print(type(data))

'''
主成分分析
本质：PCA是一种分析、简化数据集的技术
目的：是数据维数压缩、尽可能降低原始数据的维数（复杂度），损失少量信息。
作用：可以削减回归分析或聚类分析中特征数量
场景：特征数量达到上百个的时候，考虑数据的简化。数据也会改变，特征数量也会减少。
'''
def pca():
    #n_components:小数：保留的特征数量 整数：减少到的特征数量
    pca=PCA(n_components=0.9)
    data=pca.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)
    print(type(data))


if __name__ == '__main__':
    pca()