import sklearn 
import numpy as np
from sklearn.datasets import load_boston
#导入线性回归正规方程、梯度下降API
from sklearn.linear_model import LinearRegression,SGDRegressor
#数据集分割API
from sklearn.model_selection import train_test_split
#导入标准化API
from sklearn.preprocessing import StandardScaler
#导入均方误差API
from sklearn.metrics import mean_squared_error

def bostonlinear():
    #1、获取数据
    lb=load_boston()
    # ##特征值
    print(lb.data)
    ##特征对应的目标值
    print(lb.target)
    #特征名称
    print(lb.feature_names)

    #2、分割数据集为训练集合测试集
    x_train,x_test,y_train,y_test=train_test_split(lb.data,lb.target,test_size=0.25)
    #3、特种工程：标准化处理，因为线性回归模型和损失函数会受异常数据的影响。
    # #对特征值进行标准化
    std_x=StandardScaler()
    x_train=std_x.fit_transform(x_train)
    x_test=std_x.fit_transform(x_test)

    # #对目标值进行标准化，目标值是一维需要转成二维
    std_y=StandardScaler()
    y_train=std_y.fit_transform(y_train.reshape(-1,1))
    y_test=std_y.fit_transform(y_test.reshape(-1,1))

    #4、正规方程求解方式预测结果
    sgd=SGDRegressor()
    sgd.fit(x_train,y_train)
    ##查看回归系数(每个特征的权值)
    print("回归系数",sgd.coef_)
    #预测结果。因为预测的结果是标准化后的值。需要还原
    y_predict=std_y.inverse_transform(sgd.predict(x_test))
    print("测试集房子价格预测结果：",y_predict)

    #5、回归性能评估 真实值与预测值的均方误差
    print("梯度下降的均方误差值为：",mean_squared_error(std_y.inverse_transform(y_test),y_predict))

if __name__ == "__main__":
    bostonlinear()