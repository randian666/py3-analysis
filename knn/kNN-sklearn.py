#!/usr/bin/env python3
'''
假设有一名植物学爱好者对她发现的鸢尾花的品种很感兴趣。她收集了每朵鸢尾花的一些
测量数据：花瓣的长度和宽度以及花萼的长度和宽度，所有测量结果的单位都是厘米
她还有一些鸢尾花的测量数据，这些花之前已经被植物学专家鉴定为属于setosa、
versicolor 或virginica 三个品种之一。对于这些测量数据，她可以确定每朵鸢尾花所属的品
种。我们假设这位植物学爱好者在野外只会遇到这三种鸢尾花。
我们的目标是构建一个机器学习模型，可以从这些已知品种的鸢尾花测量数据中进行学
习，从而能够预测新鸢尾花的品种。
因为我们有已知品种的鸢尾花的测量数据，所以这是一个监督学习问题。在这个问题中，
我们要在多个选项中预测其中一个（鸢尾花的品种）。这是一个分类（classification）问题
的示例。可能的输出（鸢尾花的不同品种）叫作类别（class）。数据集中的每朵鸢尾花都
属于三个类别之一，所以这是一个三分类问题。
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import  train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
import numpy as np


from sklearn.neighbors import KNeighborsClassifier
#加载数据
iris_dataset=load_iris()
# print(iris_dataset)
print('数据的键值 {}'.format(iris_dataset.keys()))
print('花的品种 {}'.format(iris_dataset['target_names']))
print(type(iris_dataset['data']))
print("花的测量数据 样本数据 {} ".format(iris_dataset['data']))
print("测量的数据对应的品类 {}".format(iris_dataset['target']))

#scikit-learn 中的train_test_split 函数可以打乱数据集并进行拆分。这个函数将75% 的
# 行数据及对应标签作为训练集，剩下25% 的数据及其标签作为测试集。
#random_state 参数指定了随机数生成器的种子。这样函数输出就是固定不变的，所以这行代码的输出始终相同

X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

print('X_train shape:{}'.format(X_train.shape))
print('X_test shaper:{}'.format(X_test.shape))
print('y_train shape:{}'.format(y_train.shape))
print('y_test shaper:{}'.format(y_test.shape))
print(X_train)
print(y_train)

#把训练集的数据转化为panda进行数据观察。
# iris_dataframe=pd.DataFrame(X_train,columns=iris_dataset['feature_names'])
# grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',hist_kwds={'bins': 20}, s=60, alpha=.8,cmap=mglearn.cm3)
# plt.show()


#K近邻算法
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
clf=KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',metric_params=None, n_jobs=1, n_neighbors=1, p=2,weights='uniform')

#　做出预测
X_new = np.array([[4.6,3.2,1.4,0.3]])
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))

#评估模型
y_pred = knn.predict(X_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))


print("Test set predictions: {}".format(clf.score(X_test, y_test)))