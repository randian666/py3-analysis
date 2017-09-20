#!/usr/bin/env python3

import os

import numpy as np

import knn.kNN as knn

'''
数字识别系统
准备数据阶段
将32*32的二进制图像矩阵转换为一个1*1024的向量
'''
def img2vector(filename):
    #创建一个1*1024的numpy数组
    returnVect=np.zeros((1,1024));
    #读取文件
    with open(filename) as fr:
        for i in range(32):
            lineStr=fr.readline();#读取文本文件中的每一行
            for j in range(32):
                returnVect[0,32*i+j]=int(lineStr[j]);
    return returnVect;
'''
测试算法阶段
'''
def handwritingClassTest():
    #1、准备样本数据
    labelNums=[];#文本对应的数组列表
    #读取样本数据文件
    listdir=os.listdir('trainingDigits')
    m=len(listdir);
    dataset=np.zeros((m,1024))
    for i in range(m):
        currFileStr=listdir[i];
        labelNums.append(currFileStr.split('.')[0].split('_')[0])
        dataset[i,:]=img2vector('trainingDigits/%s'%currFileStr)
    #2、准备测试数据
    testListdir=os.listdir('testDigits')
    errorCount=0.0; #错误次数
    testM=len(testListdir)
    testDataset = np.zeros((testM, 1024))
    for j in range(testM):
        currFileStr = testListdir[j];
        currNum=int(currFileStr.split('.')[0].split('_')[0]);
        testData = img2vector('testDigits/%s' % currFileStr)
        resultNum=int(knn.classify0(testData,dataset,labelNums,3));
        if (resultNum!=currNum):
            errorCount+=1;
        print('预测结果数字为%s,实际数字为%s'%(resultNum,currNum))
    print("预测结束，错误率为：%s"%(errorCount/float(testM)))
    
if __name__ == '__main__':
    handwritingClassTest();