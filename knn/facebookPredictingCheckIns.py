#!/usr/bin/env python3
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
'''
K-近邻预测用户签到位置
数据介绍：
row_id       x       y         accuracy    time    place_id
数据ID   定位x坐标  定位y坐标 定位的准确性 时间戳 目标入住位置
'''
def knncls():
    '''
    读取数据
    '''
    data=pd.read_csv('D://pywork//data//facebook-v-predicting-check-ins//train.csv');
    # print(data.head(10))
    #处理数据
    #1、数据过大缩小数据范围,通过query查询数据进行帅选
    data=data.query("x>1.0 & x<1.25 & y>2.5 & y<2.75")

    #2、处理时间,
    time_val=pd.to_datetime(data['time'],unit='s')
    time_val=pd.DatetimeIndex(time_val)

    #3、构造特征并删除time特征
    data['day']=time_val.day
    # data['hour'] = time_val.hour
    # data['weekday']=time_val.weekday
    data=data.drop(['time'],axis=1)

    #4、把签到数据量少于N个的目标位置删除
    place_count=data.groupby('place_id').count()
    # print(place_count.head(10))
    tf_data=place_count[place_count.row_id>3].reset_index()
    # print(tf_data.head(10))
    data=data[data['place_id'].isin(tf_data.place_id)]
    data=data.drop(['row_id'],axis=1)
    print(data.head(10))
    #5、取出数据中的特征值和目标值
    y_data=data['place_id']
    x_data=data.drop(['place_id'],axis=1)
    #6、进行数据分割训练集合和测试集合
    x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.25)
    '''
    特征工程,对训练集和测试集的特征值进行标准化
    '''
    std=StandardScaler()
    x_train=std.fit_transform(x_train)
    ##训练集上调用fit_transform()，其实找到了均值μ和方差σ^2，即我们已经找到了转换规则（即方差和均值），
    # 我们把这个规则利用在训练集上，同样，我们可以直接将其运用到测试集上（甚至交叉验证集），所以在测试集上的处理，
    # 我们只需要标准化数据而不需要再次拟合数据。
    x_test=std.transform(x_test)
    '''
    算法预测、评估算法
    '''
    # knn=KNeighborsClassifier(n_neighbors=5)
    # #1、训练数据
    # knn.fit(x_train,y_train)
    # #2、进行预测
    # y_predict=knn.predict(x_test)
    # print("预测目标的签到位置：",y_predict)
    # #3、评估算法
    # score = knn.score(x_test, y_test)
    # print("准确率为：",score)
    #网格搜索参数调优
    knn=KNeighborsClassifier()
    param={"n_neighbors":[3,5,7,10,15]}
    gs=GridSearchCV(knn,param_grid=param,cv=5);
    #进行预测
    gs.fit(x_train,y_train)
    #预测准确率
    print("在测试集上准确率：",gs.score(x_test,y_test))
    print("在交叉验证当中最好的结果：",gs.best_score_)
    print("选择最好的模型是：",gs.best_estimator_)
    print("每次超参数每次交叉验证的结果：",gs.cv_results_)
if __name__ == '__main__':
    knncls()