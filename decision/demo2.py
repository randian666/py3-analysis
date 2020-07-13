#!/usr/bin/env python3
#coding:utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
'''
随机森林
泰坦尼克号数据
在泰坦尼克号和titanic2数据帧描述泰坦尼克号上的个别乘客的生存状态。在泰坦尼克号的数据帧不包含从剧组信息，
但它确实包含了乘客的一半的实际年龄。关于泰坦尼克号旅客的数据的主要来源是百科全书Titanica。
这里使用的数据集是由各种研究人员开始的。其中包括许多研究人员创建的旅客名单，由Michael A. Findlay编辑。
我们提取的数据集中的特征是票的类别，存活，乘坐班，年龄，登陆，home.dest，房间，票，船和性别。乘坐班是指乘客班（1，2，3），
是社会经济阶层的代表。其中age数据存在缺失。

随机森林参数：https://blog.csdn.net/qq_16633405/article/details/61200502
'''

def decision():
    """
    使用随机森林对泰坦尼克号进行预测生死
    :return:
    """
    #获取数据
    titan=pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt");
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
    #随机森林进行预测 n_estimators决策树数量 max_depth数的深度
    rf=RandomForestClassifier()
    param={"n_estimators":[120,200,300,500,800,1200],"max_depth":[5,8,15,25,30]}
    #网格搜索与交叉验证进行参数调优
    gc=GridSearchCV(rf,param_grid=param,cv=2)
    #进行预测
    gc.fit(x_train,y_train)
    print("准确率：",gc.score(x_test,y_test))
    print("最佳参数：",gc.best_params_)

if __name__ == '__main__':
    decision();