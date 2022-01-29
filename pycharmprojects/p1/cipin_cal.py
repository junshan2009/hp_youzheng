# !/usr/bin/env python
# -*-coding:utf-8 -*-

import jieba
import codecs

article = open('word.txt','r').read()
dele = {'。','！','？','的','“','”','（','）',' ','》','《','，'}
jieba.add_word(u'大数据')
words = list(jieba.cut(article))
articleDict = {}
articleSet = set(words)-dele
for w in articleSet:
    if len(w)>1:
        articleDict[w] = words.count(w)

articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)

for i in range(10):
    print(articlelist[i])