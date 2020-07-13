#!usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import jieba
import jieba.posseg as pseg  ##引入结巴分词词性标注
import xlrd
# 读取数据
data = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\pydemo\spiders\1.xlsx', sheet_name = '数据产品经理')


# 查看数据
data.head()
l = len(data)
df1=pd.DataFrame(columns=['word','type'])
for i in range(l):
    words = pseg.cut(data.ix[i][x]) ##x填写要分词的内容所在列数-1
    for t in words:
        df2 = pd.DataFrame([t.word,t.flag], columns=data2.columns)
        df1.append(df2,ignore_index=True)
df3=df1.groupby(['word','type']).count()