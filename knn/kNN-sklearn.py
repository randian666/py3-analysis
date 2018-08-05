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
#加载数据
iris_dataset=load_iris()
# print(iris_dataset)
print(iris_dataset.keys())
print(type(iris_dataset['data']))
print(iris_dataset['data'])
print(iris_dataset['target'])