#!/usr/bin/env python3
#coding:utf-8
'''
print(matplotlib.matplotlib_fname())
修改matplotlibrc文件
将文件中的
#font.family: sans-serif
在注释的下一行，添加一行：
font.family: Microsoft YaHei
可显示为中文

'''
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串


df=pd.read_csv("csv/xiebuyazheng.csv",header=None,encoding="utf-8")

#星星数判定评论质量 返回
datas=df[2].value_counts()
print(datas)
scale_ls = datas.index
index_ls = datas.values
print(scale_ls)
print(index_ls)
plt.bar(scale_ls, index_ls,label='Men',color='rgb')
plt.title('评论质量')
plt.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = datas.index
sizes = datas.values
# explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('评论质量')
plt.show()