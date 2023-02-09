#!/usr/bin/env python3
#coding:utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_graphviz
# 导入dot插件库
import pydotplus
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
'''
泰坦尼克号数据
在泰坦尼克号和titanic2数据帧描述泰坦尼克号上的个别乘客的生存状态。在泰坦尼克号的数据帧不包含从剧组信息，
但它确实包含了乘客的一半的实际年龄。关于泰坦尼克号旅客的数据的主要来源是百科全书Titanica。
这里使用的数据集是由各种研究人员开始的。其中包括许多研究人员创建的旅客名单，由Michael A. Findlay编辑。
我们提取的数据集中的特征是票的类别，存活，乘坐班，年龄，登陆，home.dest，房间，票，船和性别。乘坐班是指乘客班（1，2，3），
是社会经济阶层的代表。其中age数据存在缺失。
'''

def decision():
    """
    使用决策树对泰坦尼克号进行预测生死
    :return:
    """
    #获取数据
    titan=pd.read_csv("decision/titanic.csv")
    print(titan.head(10))
    # print(titan.index)
    #票的类别、年龄、性别
    x=titan[['pclass','age','sex']]
    print(x.head(10))
    #目标值是否存活
    y=titan['survived']
    #缺失值处理:默认用年龄的平均值并替换
    x['age'].fillna(x['age'].mean(),inplace=True)
    # print(x)
    # print(y)
    #分割数据集为训练集、测试集
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
    # print(x_train.to_dict(orient="records"))
    #进行处理，特种工程 特征-》类别-》One Hot编码
    dict=DictVectorizer(sparse=False)
    x_train=dict.fit_transform(x_train.to_dict(orient="records"))
    x_test=dict.transform(x_test.to_dict(orient="records"))
    print(dict.get_feature_names())
    print(x_train)
    #使用决策树进行预测
    dec=DecisionTreeClassifier();
    dec.fit(x_train,y_train)
    print("准确率：",dec.score(x_test,y_test))
    # #决策树的结构、本地保存
    # export_graphviz(dec,out_file='tree.dot',feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])
    # # 展示可视化图
    # (graph,) = pydotplus.graph_from_dot_file('tree.dot')
    # graph.write_png('tree.png')
    # 数据可视化
    plt.figure(figsize=(15,9))
    plot_tree(dec,filled=True,feature_names=dict.get_feature_names(), class_names='survived')
    plt.show()
if __name__ == '__main__':
    decision();