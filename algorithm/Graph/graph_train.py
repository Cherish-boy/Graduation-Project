import csv
import json
from random import random, randint

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Graph


# from word2vec_test import list, content_company



data = pd.read_csv("policy.csv", header=None)
list_policy = data.values.tolist()
data = pd.read_csv('company.csv', header=None)
list_company = data.values.tolist()
nodes = []
links = []
categories = []
# list_policy[randint(1, len(list_policy) - 1)][0]
# for i in range(1, len(list_policy)):
#     context = {'name': list_policy[i][0], 'symbolSize': 12, 'draggable': 'False', 'value': list_policy[i][1],
#                'category': list_policy[i][0], 'label': {'normal': {'show:True'}}}
#     nodes.append(context)
#
# for i in range(1, len(list_company)):
#     context = {'name': list_company[i][0], 'symbolSize': 12, 'draggable': 'False', 'value': 0,
#                'category': list_policy[randint(1, len(list_policy) - 1)][0], 'label': {'normal': {'show:True'}}}
#     contexts = {'source': context['category'], 'target': list_company[i][0]}
#     nodes.append(context)
#     links.append(contexts)
#
# for i in range(1, len(list_policy)):
#     content = {'name': list_policy[i][0]}
#     categories.append(content)
for i in range(1, 200):
    context = {'name': list_policy[i][0], 'symbolSize': 20, 'draggable': 'False', 'value': list_policy[i][1],
               'category': list_policy[i][0], 'label': {'normal': {'show:True'}}}
    nodes.append(context)

for i in range(1, 500):
    context = {'name': list_company[i][0], 'symbolSize': 10, 'draggable': 'False', 'value': list_company[i][1],
               'category': list_policy[randint(1, 200)][0], 'label': {'normal': {'show:True'}}}
    contexts = {'source': context['category'], 'target': list_company[i][0]}
    nodes.append(context)
    links.append(contexts)

for i in range(1, 200):
    content = {'name': list_policy[i][0]}
    categories.append(content)
print(nodes[600])
print(nodes[60])
print(links[30])
print(categories[30])
c = (
    Graph()
        .add(
        "",
        nodes,
        links,
        categories,
        repulsion=80,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
        .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="面向企业科技信息服务的可解释推荐系统"),
    )
        .render("graphsss.html")
)
