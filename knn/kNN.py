#!/usr/bin/env python3
'''
它的工作原理是：存在一个样本数据集合，也称作训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一数据与所属分类的对应关系。
输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本集中特征最相似数据（最近邻）的分类标签。
一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。

K近邻算法流程
1、收集收据
2、准备数据：距离计算所需要的数值，最好是结构化的数据格式
3、分析数据
4、训练算法：此步骤不适用于K近邻算法
5、测试算法：计算错误率
6、使用算法：首先需要输入样本数据和结构化的输出结果，然后运行K近邻算法判定输入数据分别属于哪个分类，
最后应用对计算出的分类执行后续的处理
'''

#导入numpy科学计算、运算符模块
import numpy as np
import operator
'''
创建样本数据
'''
def createDataset():
    group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

'''
4个输入参数：用户分类的输入向量是inX，输入的训练样本集为dataSet，标签向量为labels，最后k表示用于选择最近邻的数目
点与点之间的距离计算公式为√(A-B)^+(A1-B1)^
'''
def classify0(inX,dataSet,labels,k):
    datasize=dataSet.shape[0];#计算行的数量
    #计算行距离
    diffMat=np.tile(inX,(datasize,1)) -dataSet;#向量inX列重复datasize次行重复1次并且减去训练样本，保证向量的元素数目和矩阵dataSet的行数相同
    # print(diffMat)
    sqDiffMat=diffMat**2;           #每个元素的平方
    # print(sqDiffMat)
    sqDistances=sqDiffMat.sum(axis=1) #根据行求和
    # print(sqDistances)
    distances=sqDistances**0.5;  #求和后的二分之一次方,也就是平方根
    # print(distances)
    sortedDistIndicies=distances.argsort(); #返回从小到大的索引值
    # print(sortedDistIndicies)
    classCount={};
    #选择距离最小的K个点
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]] #对应的标签
        # print(voteIlabel)
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1; #确定前K个点所在类别的出现频率
    # print(classCount)
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True); #根据出现频率倒排排序
    # print(sortedClassCount)
    return sortedClassCount[0][0] #返回标签

if __name__ == '__main__':
    group,labels=createDataset()
    result=classify0([0.9,0.9],group,labels,3);
    print('该标签属于分类：',result)

