#!/usr/bin/env python3
# coding:utf-8

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import jieba

'''
文本特征处理:对文本进行特征值化。用于：文本分类、情感分析。
'''


'''
CountVectorizer
1、统计所有文章当中所有的词，重复的只看做一次。
2、每篇文章，在词的列表里面进行统计每次词出现的次数。
3、单个字母不统计
'''
def countvec():
    # 实例化CountVectorizer，统计次数
    cv = CountVectorizer()
    data = cv.fit_transform(['To let go of love is not to lose it, but to hide it in your heart.',
                             'The worst result of confession is not rejection, but the loss of a friend.'])
    new_data = data.toarray()
    print(new_data)
    print(type(new_data))
    # 输出类别名称
    print(cv.get_feature_names())
'''
中文CountVectorizer处理
'''
def countCnVec():
    # 实例化CountVectorizer，统计次数
    cv = CountVectorizer()
    # 中文要先用jieba进行分词
    con1 = jieba.cut('若不是因为爱着你，怎会不经意就叹息。')
    con2 = jieba.cut('所谓坚强，就是放弃时不放弃，该哭时不哭泣。')
    content1 = " ".join(list(con1))
    conteng2 = " ".join(list(con2))
    data = cv.fit_transform([content1, conteng2])
    new_data = data.toarray()
    print(new_data)
    print(type(new_data))
    # 输出类别名称
    print(cv.get_feature_names())
'''
TF-IDF的主要思想：如果某个词或短语在一篇文章中出现的概率高，
并且在其他文章中很少出现，则认为此词或者短语具有很好的的类别区分能力，适合用来分类。
TF-IDF作用：用以评估一个字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
TF：term frequency 词的频率
IDF：逆文档频率 inverse document frequency，公式：log(总文档数量/该词出现的文档数)
重要性公式：TF*IDF
'''
def tfidfVec():
    # 实例化TfidfVectorizer
    cv = TfidfVectorizer()
    # 中文要先用jieba进行分词
    con1 = jieba.cut('若不是因为爱着你，怎会不经意就叹息。')
    con2 = jieba.cut('所谓坚强，就是放弃时不放弃，该哭时不哭泣。')
    content1 = " ".join(list(con1))
    conteng2 = " ".join(list(con2))
    data = cv.fit_transform([content1, conteng2])
    new_data = data.toarray()
    print(new_data)
    print(type(new_data))
    # 输出类别名称
    print(cv.get_feature_names())
if __name__ == '__main__':
    tfidfVec()
