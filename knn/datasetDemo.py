#!/usr/bin/env python3

import mglearn.datasets

import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import numpy as np

def forgedataset():
    X,y=mglearn.datasets.make_forge();
    print(type(X))
    print(type(y))
    print(X)
    print(y)
    print(X[:,0])
    #X为训练集  y为数据对应的类别
    # 数据集绘图 已第一个特征作为X轴 第二个特征作为y轴 每个点对于的颜色合和形状对应其类别
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    plt.legend(["Class 0", "Class 1"], loc=4)
    plt.xlabel("First feature")
    plt.ylabel("Second feature")
    print("X.shape: {}".format(X.shape))
    plt.show()
def wavedataset():
    X,y=mglearn.datasets.make_wave(n_samples=40)
    print(X.shape)
    print(y.shape)
    print(X)
    print(y)
    plt.plot(X, y, 'o')
    plt.ylim(-3, 3)
    plt.xlabel("Feature")
    plt.ylabel("Target")
    plt.show()
def cancerdataset():
    cancer=load_breast_cancer()
    print("cancer.keys(): {}".format(cancer.keys()))
    print("cancer.data.shape: {}".format(cancer.data.shape))
    print("cacancer.target.shape:{}".format(cancer.target.shape))
    print(cancer.target_names)
    print(cancer.target)
    #统计每个分类出现的次数
    print(np.bincount(cancer.target))
    print(list(zip(cancer.target_names,np.bincount(cancer.target))))
    print("Sample counts per class:\n{}".format({n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))

    print("Feature names:\n{}".format(cancer.feature_names))

    mglearn.plots.plot_knn_classification(n_neighbors=1)
if __name__ == '__main__':
    cancerdataset()
