#!/usr/bin/env python3

import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

'''
NumPy绘制图形
'''

def demo1():
    fig = plt.figure(2)  # 指定编号
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    print(randn(50).cumsum())
    plt.plot(randn(50).cumsum(), 'k--')  # plt就会在最后一个用过的subplot上进行绘制，k--是线型选项，用于绘制黑色虚线
    # 可以在指定的subplot上进行绘制
    ax1.hist(randn(100), bins=20, color='k', alpha=0.3)  # 柱状图
    ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))  # 散点图
    plt.show()
def demo2():
    '''
    subplots可以创建一个新的figure，并返回一个含有已创建的subplot对象的Numpy数组
    sharex 所有的subplot使用相同的X轴刻度
    sharey 所有的subplot使用相同的Y轴刻度
    '''
    fig,axes=plt.subplots(2,2,sharex=True,sharey=True) #创建两行两列的图
    for i in range(2):
        for j in range(2):
            axes[i,j].hist(randn(100), bins=20, color='k', alpha=0.3)  # 柱状图
    plt.subplots_adjust(wspace=0,hspace=0) #图与图之间的宽度、高度的百分比
    plt.show();
def demo3():
    fig = plt.figure()  # 指定编号
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.plot(randn(10).cumsum(),'g--')  #绘制绿色的虚线
    ax2.plot(randn(10).cumsum(),color='g',linestyle='--',marker='o',label='steps-post')  #绘制绿色以及带有标记数据点的虚线
    plt.show();
def demo4():
    fig=plt.figure();
    ax=fig.add_subplot(111);
    # ax.set_xticks([0,0.1,0.2,0.3,0.4]); #设置x轴刻度
    # ax.set_yticks([0,0.1,0.2,0.3,0.4]) #设置y轴刻度
    # ax.set_xticklabels(['a','b','c','d','e']); #x轴刻度标签
    ax.set_title('my name tisck') #图标题
    ax.set_xlabel('Stages');  #x轴标签
    ax.plot(randn(1000).cumsum(),'r--',label='two') #添加数据
    ax.plot(randn(1000).cumsum(),'k--',label='three') #添加数据
    plt.savefig('firstpath.png') #保存图片到本地，还可以保存到StringIOs流中
    plt.show();
if __name__ == '__main__':
    demo4();