#!/usr/bin/env python3

'''
读取文件，将待处理的数据格式转换成分类器可以接受的格式。
返回测试样本、以及样本对应的标签数据
'''
import numpy as np
import matplotlib.pyplot as plt
import knn.kNN as knn

def file2martrix(filename):
    with open(filename) as fr:
        arrayOlines=fr.readlines();
        #文件的行数
        numberOfLines=len(arrayOlines);
        #创建一个0填充的矩阵NumPy
        returnMat=np.zeros((numberOfLines,3))
        #标记
        classLabelVector=[]
        index=0
        for line in arrayOlines:
            line=line.strip() #去掉前后空格
            listFromLine=line.split('\t');
            returnMat[index,:]=listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1])) #标签
            index+=1;
        return returnMat,classLabelVector;
'''
将任意取值范围的特征值转化为0到1区间内的值
newValue=（OldValue-min）/(max-min)
'''
def autoNorm(dataset):
    minVals=dataset.min(0); #每列中最小的数
    maxVals=dataset.max(0); #每列中最大的数
    ranges=maxVals-minVals; #取值范围
    normDataSet=np.zeros(np.shape(dataset)); #生成一个维度以样本集合0填充的矩阵，
    m=dataset.shape[0] #样本集合行数
    normDataSet=dataset-np.tile(minVals,(m,1)) #样本集合减去样本中最小的数
    normDataSet=normDataSet/np.tile(ranges,(m,1)) #特征值相除
    return normDataSet,ranges,minVals;
'''
样本分类标签散点图
'''
def pltShow():
    returnMat, classLabelVector=file2martrix('datingTestSet2.txt');
    normDataSet, ranges, minVals=autoNorm(returnMat)

    fig=plt.figure();
    ax=fig.add_subplot(111);
    # 散点图使用returnMat矩阵的第1、第2列数据，分别表示特征值“每年获得的飞行常客里程数比”和“玩视频游戏所耗时间百分比”
    # 使用classLabelVector存储的标签属性，在散点图上绘制了色彩不等，尺寸不同的点。
    ax.scatter(normDataSet[:,0],normDataSet[:,1],15.0*np.array(classLabelVector),15.0*np.array(classLabelVector))
    plt.show();
'''
测试算法：验证分类器
'''
def datingClassTest():
    returnMat, classLabelVector = file2martrix('datingTestSet2.txt');
    normDataSet, ranges, minVals = autoNorm(returnMat)
    hoRatio = 0.40;
    m = normDataSet.shape[0];
    numTestVecs = int(m * hoRatio);  # 测试次数
    errorCount = 0;
    for i in range(numTestVecs):
        # 前numTestVecs个作为测试数据，其他的作为训练样本数据。
        classResult = knn.classify0(normDataSet[i, :], normDataSet[numTestVecs:m, :], classLabelVector[numTestVecs:m],3)
        print('the classify0 came back with:%s,the real answer is %s' % (classResult, classLabelVector[i]))
        if (classResult != classLabelVector[i]):
            errorCount += 1;
    print("the total error rate is %s" % (errorCount / float(numTestVecs)))
'''
使用算法
构建一个可用系统
'''
def classifyPerson():
    resultList=['不喜欢的人','魅力一般的人','极具魅力的人'];
    ffmiles = float(input("每年获得的飞行常客里程数?"))
    percentTats=float(input("玩视频游戏所耗时间百分比?"))
    iceCream = float(input("每周消费的冰琪淋公升数?"))
    returnMat, classLabelVector = file2martrix('datingTestSet2.txt');
    normDataSet, ranges, minVals = autoNorm(returnMat)
    inArry=np.array([ffmiles,percentTats,iceCream])
    classResult = knn.classify0((inArry-minVals)/ranges,normDataSet,classLabelVector,3)
    print('classResult=',classResult)
    print("这是你喜欢的人吗？答案是：",resultList[classResult-1])
if __name__ == '__main__':
    '''
    数据文件说明：
    每年获得的飞行常客里程数
    玩视频游戏所耗时间百分比
    每周消费的冰琪淋公升数
    不喜欢的人、魅力一般的人、极具魅力的人
    '''
    # datingClassTest();
    # pltShow();
    classifyPerson();