#导入xgboost工具
import pandas as pd
import xgboost as xgb
import time
#导入计算分类正确率工具
from sklearn.metrics import accuracy_score


#训练集
dtrain=xgb.DMatrix('D:/pywork/py3-analysis/xgb/data/agaricus.txt.train')
#测试集
dtest=xgb.DMatrix('D:/pywork/py3-analysis/xgb/data/agaricus.txt.test')
print(dtrain.num_col())
print(dtrain.num_row())

# max_depth： 树的最大深度。缺省值为6，取值范围为：[1,∞]
# eta：为了防止过拟合，更新过程中用到的收缩步长。在每次提升计算之后，算法会直接获得新特征的权重。 
# eta通过缩减特征的权重使提升计算过程更加保守。缺省值为0.3，取值范围为：[0,1]
# silent：取0时表示打印出运行时信息，取1时表示以缄默方式运行，不打印运行时信息。缺省值为0
# objective： 定义学习任务及相应的学习目标，“binary:logistic” 表示二分类的逻辑回归问题，输出为概率。

#xgboost参数
param = {'max_depth':2, 'eta':1, 'silent':0, 'objective':'binary:logistic' }

# 设置boosting迭代计算次数
num_round = 2

#构建训练模型
starttime=time.clock()
bst=xgb.train(param,dtrain,num_round)# dtrain是训练数据集
endtime=time.clock()
print ('耗时：',(endtime - starttime))

# XGBoost预测的输出是概率。这里蘑菇分类是一个二类分类问题，输出值是样本为第一类的概率。
train_preds=bst.predict(dtrain)
print("train_preds",train_preds)
#我们需要将概率值转换为0或1。
train_predictions = [round(value) for value in train_preds]
print ("train_predictions",train_predictions)

#特征实际对应的标签
y_train=dtrain.get_label()
print ("y_train",y_train)

#计算正确率
train_accuracy = accuracy_score(y_train, train_predictions)
print ("Train Accuary: %.2f%%" % (train_accuracy * 100.0))


#利用测试集进行测试
preds =bst.predict(dtest)
predictions = [round(value) for value in preds]
y_test = dtest.get_label()
test_accuracy = accuracy_score(y_test, predictions)
print("Test Accuracy: %.2f%%" % (test_accuracy * 100.0))

# 模型可视化需要安装graphviz
# from matplotlib import pyplot
# import graphviz
 
# xgb.plot_tree(bst,num_trees=1, rankdir= 'LR' )
# pyplot.show()
# xgb.to_graphviz(bst,num_trees=0)
# xgb.to_graphviz(bst,num_trees=1)











