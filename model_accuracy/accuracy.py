import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score,roc_curve

'''
accuracy_score:
分类准确率分数是指所有分类正确的百分比。分类准确率这一衡量分类器的标准比较容易理解，
但是它不能告诉你响应值的潜在分布，并且它也不能告诉你分类器犯错的类型。

API:    
sklearn.metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
normalize：默认值为True，返回正确分类的比例；如果为False，返回正确分类的样本数
'''
def accuracy_score_demo():
    y_pred = [0, 2, 1, 3]
    y_true = [0, 1, 2, 3]
    print(accuracy_score(y_true,y_pred))
    print(accuracy_score(y_true,y_pred,normalize=False))

'''
recall_score:
召回率 =提取出的正确信息条数 /样本中的信息条数。通俗地说，就是所有准确的条目有多少被检索出来了。

API:    
klearn.metrics.recall_score(y_true, y_pred, labels=None, pos_label=1,average='binary', sample_weight=None)
参数average : string, [None, ‘micro’, ‘macro’(default), ‘samples’, ‘weighted’]

'''
def recall_score_demo():
    y_pred = [0, 2, 1, 3]
    y_true = [0, 1, 2, 3]
    print(recall_score(y_true, y_pred, average='macro'))

'''
roc_curve:
ROC曲线指受试者工作特征曲线/接收器操作特性(receiver operating characteristic，ROC)曲线，是反映灵敏性和特效性连续变量的综合指标，是用构图法揭示敏感性和特异性的相互关系，
它通过将连续变量设定出多个不同的临界值，从而计算出一系列敏感性和特异性。ROC曲线是根据一系列不同的二分类方式（分界值或决定阈），
以真正例率（也就是灵敏度）（True Positive Rate,TPR）为纵坐标，假正例率（1-特效性）（False Positive Rate,FPR）为横坐标绘制的曲线。
API:
sklearn.metrics.roc_curve(y_true,y_score, pos_label=None, sample_weight=None, drop_intermediate=True)
该函数返回这三个变量：fpr,tpr,和阈值thresholds
thresholds：
分类器的一个重要功能“概率输出”，即表示分类器认为某个样本具有多大的概率属于正样本（或负样本）。

'''
def roc_curve_demo():
    y = np.array([0, 2, 1, 3])
    y_scores = np.array([0, 1, 2, 3])
    fpr, tpr, thresholds = roc_curve(y, y_scores, pos_label=2)
    print(fpr)
    print(tpr)
    print(thresholds)
    print("threshold : ", thresholds[np.argmax(abs(tpr - fpr))])

'''
roc_auc_score:
直接根据真实值（必须是二值）、预测值（可以是0/1,也可以是proba值）计算出auc值，中间过程的roc计算省略。

API:
sklearn.metrics.roc_auc_score(y_true, y_score, average='macro', sample_weight=None)
average : string, [None, ‘micro’, ‘macro’(default), ‘samples’, ‘weighted’]

'''
def roc_auc_score_demo():
    y_true = np.array([0, 0, 1, 1]) 
    y_scores = np.array([0, 0.4, 0.35, 0.8]) 
    print(roc_auc_score(y_true, y_scores))

if __name__ == "__main__":
    roc_auc_score_demo()




