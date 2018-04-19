#!/usr/bin/env python3

import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
'''
pandas中绘制图
'''
def demo1():
    s=Series(randn(10).cumsum(),index=np.arange(0,100,10))
    s.plot();
    plt.show()
def demo2():
    data=DataFrame(np.random.randn(10,4).cumsum(0),columns=['a','b','c','d'],index=np.arange(0,100,10))
    data.plot(style='o--');
    plt.show()
'''
柱状图绘制
'''
def demo3():
    fig,axs=plt.subplots(2,1)
    s=Series(np.random.randn(16),index=range(16))
    s.plot(kind='bar',ax=axs[0],color='g',alpha=0.7); #kind图的形状，ax指定的图上进行绘制，color颜色，alpha透明度
    s.plot(kind='barh', ax=axs[1], color='g', alpha=0.7);
    plt.show()
def demo4():
    fig,axs=plt.subplots(2,1)
    s=DataFrame(np.random.randn(6,4),index=list('abcdef'),columns=['one','two','three','four'])
    s.plot(kind='bar',ax=axs[0],color='g',alpha=0.7); #kind图的形状，ax指定的图上进行绘制，color颜色，alpha透明度
    s.plot(kind='barh', ax=axs[1], color='g', alpha=0.7);
    plt.show()

if __name__ == '__main__':
    demo4();