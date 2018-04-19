#!/usr/bin/env python3
#coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
柱状图
'''
def barh():
    df=pd.read_excel('csv/0301~0320.xls')
    df.index=df['分类名称'].values #第一列分类名称作为index
    newdf=df.drop("分类名称",axis=1) #删除第一列
    print(newdf)
    newdf.plot(kind='barh',align='center',color = 'c')
    plt.rcParams['font.sans-serif']=['SimHei']#中文编码
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.title('20180301-20180320一级品类拉新用户')

    # df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    # df2.plot(kind='bar')  # 分开并列线束
    # df2.plot(kind='bar', stacked=True)  # 四个在同一个里面显示 百分比的形式
    # df2.plot(kind='barh', stacked=True)  # 纵向显示
    plt.show()
def barh2():
    df=pd.read_excel('csv/20180325渠道领券量指标数据.xls')
    df.index=df['渠道名称'].values #第一列分类名称作为index
    newdf=df.drop("渠道名称",axis=1) #删除第一列
    # print(newdf)
    newdf.plot(kind='barh',align='center',color = 'c',sharey=True)
    plt.rcParams['font.sans-serif']=['SimHei']#中文编码
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.title('20180325渠道领券量指标数据')
    plt.show()
if __name__ == '__main__':
    # barh();
    barh2();
