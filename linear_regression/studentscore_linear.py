import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#1.导入数据集,数据地址：https://github.com/MLEveryday/100-Days-Of-ML-Code/tree/master/datasets
dataset=pd.read_csv('data\studentscores.csv')
#特征
X = dataset.iloc[ : ,   : 1 ].values
#目标值
Y = dataset.iloc[ : , 1 ].values
print(X)
print(Y)

#2.数据集分割，训练集和测试集
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

#3.训练集使用简单线性回归模型来训练
regression=LinearRegression()
regression.fit(x_train,y_train)

#4.预测结果
Y_pred=regression.predict(x_test)

print("测试特征值：")
print(x_test)
print("测试目标值：")
print(y_test)
print("测试数据预测结果：")
print(Y_pred)

#5.可视化
#训练集结果可视化
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train , regression.predict(x_train), color ='blue')
plt.show()

#测试集结果可视化
plt.scatter(x_test , y_test, color = 'red')
plt.plot(x_test , regression.predict(x_test), color ='blue')
plt.show()