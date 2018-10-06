# -*- coding: utf-8 -*-/
"""
Created on Fri Oct  5 23:02:51 2018

@author: Administrator
"""

import jieba
sentence="我喜欢上海东方明珠"
w1=jieba.cut(sentence,cut_all=True)
for item in w1:
    print(item)
sentence="我喜欢上海东方明珠"
w2=jieba.cut(sentence,cut_all=False)
for item in w2:
    print(item)
    
sentence="我喜欢上海东方明珠"
w2=jieba.cut_for_search(sentence)
for item in w2:
    print(item)
data11=open("D:/Downloads/盗墓笔记全集.txt").read().encoding='gbk')
file = open("D:/Downloads/盗墓笔记全集.txt", encoding='gbk')
data=file.read()
file2=open(file).read().decode('gb18030','ignore')
path = 'D:/Downloads/dmbj.txt'
file = open(path, encoding='gb18030', errors='ignore')
data=file.read()
file2 = open('D://Document And Settings3/lqz/Desktop/Walden2.txt', 'w')
file2.write(file.read())
file.close()
file2.close()
with open('D://Document And Settings3/lqz/Desktop/Walden2.txt', 'r') as text:
    words = text.read().split()
    print(words)
    for word in words:
        print('{}-{} times'.format(word, words.count(word)))
import jieba.analyse
tag=jieba.analyse.extract_tags(data,30)
print(tag)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim
from gensim import corpora,models,similarities
from collections import  defaultdict
import jieba
doc1="G:/d1.txt"
doc2="G:/d2.txt"
d1=open(doc1).read()
d2=open(doc2).read()
data1=jieba.cut(d1)
data11=" "
for item in data1:
    data11+=item+" "
data22=" "
data2=jieba.cut(d2)
for item in data2:
    data22+=item+" "
documents=[data11,data22]
texts=[[word for word in document.split()] for document in documents]
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1

'''去掉频率低的次
texts=[[word for word in text if frequency[token]>3]
for text in texts]'''
'''建立语料库'''

dictionary=corpora.Dictionary(texts)

doc3="G:/d3.txt"
d3=open(doc3).read()
data3=jieba.cut(d3)
data33=" "
for item in data3:
    data33+=item+" "
new_doc=data33
new_vec=dictionary.doc2bow(new_doc.split())
corpus=[dictionary.doc2bow(text) for text in texts]
tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vec]]
print(sim)







from gensim import corpora, models, similarities
import jieba
def cut(sentence):
    generator = jieba.cut(sentence)
    return [word for word in generator]
doc1="G:/d1.txt"
doc2="G:/d2.txt"
d1=open(doc1).read()
d2=open(doc2).read()
data1=jieba.cut(d1)
data11=" "
for item in data1:
    data11+=item+" "
data22=" "
data2=jieba.cut(d2)
for item in data2:
    data22+=item+" "
doc3="G:/d3.txt"
d3=open(doc3).read()
data3=jieba.cut(d3)
data33=" "
for item in data3:
    data33+=item+" "
keyword =d33
texts = [cut(text) for text in texts]
dictionary = corpora.Dictionary(texts)
feature_cnt = len(dictionary.token2id.keys())
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
new_vec = dictionary.doc2bow(cut(keyword))
# 相似度计算
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
print('\nTF-IDF模型的稀疏向量集：')
for i in tfidf[corpus]:
    print(i)
print('\nTF-IDF模型的keyword稀疏向量：')
print(tfidf[new_vec])
print('\n相似度计算：')
sim = index[tfidf[new_vec]]
for i in range(len(sim)):
    print('第', i+1, '句话的相似度为：', sim[i])



















