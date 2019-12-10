
from os import path
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import pandas as pd

# 创建停用词列表

def stopwordslist():
    stopwords = [line.strip() for line in open('chinsesstoptxt.txt', encoding='UTF-8').readlines()]
    return stopwords
# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
if __name__ == '__main__':
    df=pd.read_csv("csv/xiebuyazheng.csv",header=None,encoding="utf-8")
    cut_text=''
    for row in df[0].values:
        cut_text +=seg_sentence(row)
    cloud = WordCloud(
        font_path='simhei.ttf',  # 字体最好放在与脚本相同的目录下，而且必须设置
        background_color='white',
        max_words=2000,
        max_font_size=100
    )
    word_cloud = cloud.generate(cut_text)
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()