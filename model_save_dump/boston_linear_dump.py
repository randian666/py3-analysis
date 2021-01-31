import sklearn 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
#导入线性回归正规方程、梯度下降API
from sklearn.linear_model import LinearRegression,SGDRegressor
#数据集分割API
from sklearn.model_selection import train_test_split
#导入标准化API
from sklearn.preprocessing import StandardScaler
#导入均方误差API
from sklearn.metrics import mean_squared_error

import random

#模型保存、加载
import joblib

def bostonlinear():
   #1、获取数据
    lb=load_boston()
    # ##特征值
    print(lb.data)
    ##特征对应的目标值
    print(lb.target)
    #特征名称
    print(lb.feature_names)
    x_test=lb.data[5]
    y_test=lb.target[5]


    print(x_test)
    print(y_test)
    #3、特种工程：标准化处理，因为线性回归模型和损失函数会受异常数据的影响。
    # #对特征值进行标准化
    std_x=StandardScaler()
    x_test=std_x.fit_transform([x_test])

    # #对目标值进行标准化，目标值是一维需要转成二维
    std_y=StandardScaler()
    y_test=std_y.fit_transform(y_test.reshape(-1,1))

    #载入模型
    model=joblib.load("./temp/lr_20210131.pkl");
    #预测房价结果
    predict_data=model.predict(x_test)
    print("利用保存后的模型预测出来的原始结果")
    print(predict_data)
    y_predict=std_y.inverse_transform(predict_data)
    print("利用保存后的模型预测出来的结果")
    print(y_predict)
if __name__ == "__main__":
    bostonlinear()