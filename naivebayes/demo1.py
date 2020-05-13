#!/usr/bin/env python3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def naivebayes():
    '''
    朴素贝叶斯进行文本分类
    :return:
    '''
    news=fetch_20newsgroups(subset='all')
    print(news.keys())
    print("获取特征值")
    print(news['data'][:2])
    print(news['filenames'][:2])
    print("获取目标值")
    print(news['target'][:2])
    print(news['target_names'][:2])
    #数据分割为训练集、测试集
    x_train,x_test,y_train,y_test=train_test_split(news['data'],news['target'],test_size=0.25)
    # #特征抽取
    tf=TfidfVectorizer();
    # #以训练集当中的词的列表进行每篇文章重要性统计
    x_train=tf.fit_transform(x_train)
    x_test=tf.transform(x_test)
    #
    mlt=MultinomialNB(alpha=1.0)
    mlt.fit(x_train,y_train)
    y_predict=mlt.predict(x_test)
    print("预测的文章类别：",y_predict)
    # # #准确率
    print("预测准确率：",mlt.score(x_test,y_test))
if __name__ == '__main__':
    naivebayes();