#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
"""
1、初识数据，获取数据集 返回的是Bunch类型的数据集跟字典类似
"""
print("------------------------------------------begin初识数据------------------------------------------")
iris_dataset=load_iris();
print(type(iris_dataset))
#数据集中的keys
print(iris_dataset.keys())
#DESCR 数据集简要说明；
# print(iris_dataset["DESCR"])
#target_names键对应的值是一个字符串数组，里面就是花的品种；
print(iris_dataset['target_names'])
#feature_names键对应的是一个字符串列表 数据包含在target 和data 字段中。data 里面是花萼长度、花萼宽度、花瓣长度、花瓣宽度的测量数据，格式为NumPy 数组
print(iris_dataset['feature_names'])
#data 数组的每一行对应一朵花，列代表每朵花的四个测量数据
print(iris_dataset['data'][:5])
#target 数组包含的是测量过的每朵花的品种，也是一个NumPy 数组,品种被转换成从0 到2 的整数,：0 代表setosa，1 代表versicolor，2 代表virginica
print(iris_dataset['target'])
print("------------------------------------------end初识数据------------------------------------------")
"""
2、训练数据与测试数据构建
scikit-learn 中的train_test_split 函数可以打乱数据集并进行拆分。这个函数将75% 的
行数据及对应标签作为训练集，剩下25% 的数据及其标签作为测试集。训练集与测试集的
分配比例可以是随意的，但使用25% 的数据作为测试集是很好的经验法则。
"""
print("------------------------------------------begin训练数据与测试数据构建------------------------------------------")
#X_train为data的训练集X_test为data的测试集；Y_train为target的训练集Y_test为taget的测试集
X_train,X_test,Y_train,Y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)
print("------------------------------------------end训练数据与测试数据构建------------------------------------------")
"""
3、观察数据
在构建机器学习模型之前，通常最好检查一下数据，看看如果不用机器学习能不能轻松完
成任务，或者需要的信息有没有包含在数据中。通过可视化来检查数据。
"""
print("------------------------------------------begin观察数据------------------------------------------")
iris_dataframe=pd.DataFrame(X_train,columns=iris_dataset['feature_names'])
print(iris_dataframe)
# 利用DataFrame创建散点图矩阵，按Y_train(标签)着色
grr = pd.plotting.scatter_matrix(iris_dataframe,marker='o',figsize=(15, 15),c = Y_train,hist_kwds={'bins':20},s=60, alpha=.8)
plt.show()
print("------------------------------------------end观察数据------------------------------------------")
"""
4、构建第一个模型
k 近邻分类器，构建此模型只需要保存训练集即可。要对一个新的数据点做出预测，算法会在训练集中寻找与这个新数据点距离最近
的数据点，然后将找到的数据点的标签赋值给这个新数据点。
"""
print("------------------------------------------begin构建第一个模型------------------------------------------")
knn=KNeighborsClassifier(n_neighbors=1)
#，输入参数为X_train 和y_train，二者都是NumPy 数组，前者包含训练数据，后者包含相应的训练标签
knn.fit(X_train,Y_train)
#做出预测
X_new=np.array([[5,2.9,1,0.2]])
predictResult=knn.predict(X_new)
print(predictResult)
print(iris_dataset['target_names'][predictResult])
print("------------------------------------------end构建第一个模型------------------------------------------")
"""
5、评估模型
由于测试集没有用于构建模型，但我们知道测试集中每朵鸢尾花的品种。
因此，我们可以对测试数据中的每朵鸢尾花进行预测，并将预测结果与标签（已知的品
种）进行对比。我们可以通过计算精度（accuracy）来衡量模型的优劣，精度就是品种预
测正确的花所占的比例
"""
Y_pred=knn.predict(X_test)
print(Y_pred)
print("Test score:{}".format(np.mean(Y_pred==Y_test)))