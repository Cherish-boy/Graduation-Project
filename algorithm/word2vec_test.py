import math

import jieba
import numpy as np
from gensim.models import Word2Vec
import pandas as pd
from scipy.linalg import norm
import re
import time

WORD2VEC_MODEL_DIR = './zhwiki.word2vec.model'
word2vec_model = Word2Vec.load(WORD2VEC_MODEL_DIR)


def vector_similarity(s1, s2):
    s1.replace(' ', '').replace('\u3000', '').replace('\xa0', '').replace('', '')
    s2.replace(' ', '').replace('\u3000', '').replace('\xa0', '').replace('', '')

    def sentence_vector(s):
        words = jieba.lcut(s)
        stopwords = [line.strip() for line in open('hit_stopwords.txt', 'r', encoding='utf-8').readlines()]
        v = np.zeros(400)
        for word in words:
            if word not in stopwords:
                if word2vec_model.wv[word] is not 0:
                    v += word2vec_model.wv[word]
        # print(s)
        # print(v)
        if np.all(v == 0):
            return 0
        else:
            v /= len(words)
            return v

    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    # print(v1)
    # print(v2)
    if v2 is not 0:
        return np.dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0


with open(r'company.txt', 'r', encoding='utf-8') as file:
    content_list_one = file.readlines()  # 读取所有行并返回列表

content_company = [x.strip() for x in content_list_one]

for i in range(0, len(content_company)):
    content_company[i] = re.sub('[a-zA-Z0-9#]', '', content_company[i])
data = pd.read_csv("policy导出.csv", header=None)
list = data.values.tolist()
for i in range(0, len(list)):
    list[i] = str(list[i]).replace('\u3000', '').replace('\xa0', '').replace(' ', '').replace('2', '')
    list[i] = re.sub('[a-zA-Z0-9#]', '', list[i])

result = np.zeros((len(content_company)+100, len(list)+100))
for i in range(500, 1000):
    for j in range(0, len(list)):
        if len(content_company[i]) < 10 or len(list[j]) < 10:
            continue
        # print(list[j])
        # print(content_company[i])
        result[i][j] = vector_similarity(list[i], content_company[j])
        print(i)
        print('and')
        print(j)
        print(result[i][j])
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())+'第'+str(i)+'条政策'+'/'+str(500)+'   '+str(j)+'/'+str(500))
result = pd.DataFrame(result)
result.to_csv('result_test.csv', encoding='utf-8')
