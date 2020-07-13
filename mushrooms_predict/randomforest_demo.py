'''
数据集：https://archive.ics.uci.edu/ml/datasets/Mushroom
使用随机森林对蘑菇进行分类
'''


import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.metrics import accuracy_score
#标准化
from sklearn.preprocessing import LabelEncoder
#数据分割训练集、测试集
from sklearn.model_selection import train_test_split
#导入随机森林模型
from sklearn.ensemble import RandomForestClassifier

#1、数据获取、分析
data=pd.read_csv("D:/pywork/py3-analysis/mushrooms_predict/data/mushrooms.csv")
print(data.head(10))
#查看是否有空的数据
print(data.isnull().sum())
#查看是否有异常目标值。
print(data['class'].unique())

#2、标准化标签，将标签值统一转换成range(标签值个数-1)范围内
le=LabelEncoder()
for col in data.columns:
    data[col]=le.fit_transform(data[col])

#3、获取数据把数据特征和目标值进行分离，并划分训练集、测试集
print(data.shape)
X=data.iloc[:,1:23]  #获取1-23列特征

Y=data.iloc[:, 0] #获取0列目标值
print(X.head(1))
print(Y.head(1))

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=4)

#4、随机森林：模型训练
model_RR=RandomForestClassifier()
model_RR.fit(x_train,y_train)
# y_prob = model_RR.predict_proba(x_test)[:,1] # This will give you positive class prediction probabilities
# y_pred = np.where(y_prob > 0.5, 1, 0) # This will threshold the probabilities to give class predictions.
# auc_roc=metrics.roc_auc_score(y_test,y_pred)
# print("准确率：",model_RR.score(x_test, y_pred))
print("准确率2：",model_RR.score(x_test,y_test))

