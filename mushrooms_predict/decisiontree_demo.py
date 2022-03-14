'''
数据集：https://archive.ics.uci.edu/ml/datasets/Mushroom
使用决策树对蘑菇进行分类
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#标准化
from sklearn.preprocessing import LabelEncoder
#数据分割训练集、测试集
from sklearn.model_selection import train_test_split
#导入决策树框架
from sklearn.tree import DecisionTreeClassifier

#1、数据获取、分析
data=pd.read_csv("mushrooms_predict/data/mushrooms.csv")
print(data.head(10))
print(type(data))
#检查每个特征有没有空值
print(data.isnull().sum())
#检查蘑菇的种类是否只有：有毒、可使用
print(data['class'].unique())
# print(data.dtypes)

#22个特征+第一个是标签 共8124个样例  
print(data.shape)

#2、标准化标签，将标签值统一转换成range(标签值个数-1)范围内
le=LabelEncoder()
for col in data.columns:
    data[col]=le.fit_transform(data[col])

print(data.head())

#3、获取数据把数据特征和目标值进行分离，并划分训练集、测试集
X=data.iloc[:,1:23]  #获取1-23列特征
Y=data.iloc[:, 0] #获取0列目标值
print(X.head(1))
print(Y.head(1))

#训练集、测试集划分
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=4)
print(x_train.shape)
print(x_test.shape)

#4、决策树：模型训练
decision_tree=DecisionTreeClassifier()
decision_tree.fit(x_train,y_train)
# y_predict=decision_tree.predict(x_test)
# print("准确率：",decision_tree.score(x_test,y_test))

#5、模型预测、评分
# predict_proba返回的是一个 n 行 k 列的数组， 第 i 行 第 j 列上的数值是模型预测 第 i 个预测样本为某个标签的概率，并且每一行的概率和为1。
y_proba=decision_tree.predict_proba(x_test)[:,1]
#预测的概率大于0.5的用1表示其他的用0表示
y_pred = np.where(y_proba > 0.5, 1, 0)
print(y_proba)
print(y_pred)
print("准确率：",decision_tree.score(x_test, y_pred))








