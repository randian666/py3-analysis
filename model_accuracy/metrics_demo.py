'''
来源：
https://zhuanlan.zhihu.com/p/234533748
'''

from sklearn import metrics
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题


y_true=[1,1,0,1,1]
y_pred=[0,0,0,1,0]

# 混淆矩阵
C = metrics.confusion_matrix(y_true, y_pred)
print("混淆矩阵为：\n",C)
# 计算准确率（accuracy）- 预测正确的占比
accuracy = metrics.accuracy_score(y_true,y_pred)
print("准确度为：\n",accuracy)
# 计算精确率（precision）-在真实值为正的样本中，预测正确的样本占比
precision = metrics.precision_score(y_true,y_pred)
print("精确率为：\n",precision)
# 计算召回率（recall） - 在预测值为正的样本中，预测为正的样本占比
recall = metrics.recall_score(y_true,y_pred)
print("召回率为：\n",recall)
# 计算F1-score（F1-score）是统计学中用来衡量二分类模型精确度的一种指标。它同时兼顾了分类模型的准确率和召回率。F1分数可以看作是模型准确率和召回率的一种加权平均，它的最大值是1，最小值是0
F1_score = metrics.f1_score(y_true,y_pred)
print("精确率为：\n",F1_score)

# 绘制PR曲线
y_pred = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1] 
y_true = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

precision,recall,thresholds = metrics.precision_recall_curve(y_true, y_pred)
plt.plot(precision, recall)
plt.title("PR Curve")
plt.xlabel("recall")
plt.ylabel("precision")
plt.show()

# 绘制ROC曲线
y_pred = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1] 
y_true = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

FPR,TPR,thresholds = metrics.roc_curve(y_true,y_pred)
print("FPR:",FPR)
print("TPR:",TPR)
plt.plot(FPR, TPR)
plt.title("ROC Curve")
plt.xlabel("recall")
plt.ylabel("precision")
plt.plot([0,1],[0,1],'r--') 
plt.show()

# 计算AUC值
y_true = [0, 0, 1, 1, 0]
y_scores = [0.1, 0.4, 0.35, 0.8, 0.2]
print('AUC socre:',metrics.roc_auc_score(y_true, y_scores))

# 计算ks值
y_pred = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1] 
y_true = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
FPR,TPR,thresholds = metrics.roc_curve(y_true,y_pred)
accuracy = metrics.accuracy_score(y_true,y_pred)
print("准确度为：\n",accuracy)
print("真正率（TPR）:",TPR)
print("伪正率（FPR）:",FPR)
print("thresholds:",thresholds)

# 绘制KS曲线
plt.title("KS Curve")
plt.plot(thresholds, FPR)
plt.plot(thresholds, TPR)
plt.show()

KS=abs(FPR-TPR).max() 
print('KS值：',KS)