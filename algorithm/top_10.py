import json

import pandas as pd
import numpy as np
import heapq

import pymysql
from pyecharts import options as opts
from pyecharts.charts import Graph


def top_ten(file):
    data = pd.read_csv(file)
    data = np.array(data)
    index = []
    max_number_list = []
    for i in range(0, len(data)):
        datas = data[i].tolist()
        max_number = heapq.nlargest(11, datas)
        # 最大的2个数对应的，如果用nsmallest则是求最小的数及其索引
        max_index = map(datas.index, heapq.nlargest(11, datas))
        # max_index 直接输出来不是数，使用list()或者set()均可输出
        # print(list(set(max_index)))
        # 序号3 索引 index 值 max_number
        # print(max_number)  # top_10得分
        index.append(list(max_index))
        max_number_list.append(max_number)
    # print(index)
    # print(max_number_list)
    return index, max_number_list


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def data_json(name, indexs, max_numbers):
    con_engine = pymysql.connect(host='8.142.138.101',
                                 user="root",
                                 password="0552fe7ad2067bda",
                                 database="database",
                                 port=3306,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = con_engine.cursor()
    sql = "select number from company where name = " + '"' + name + '"'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    number = result[0]['number']
    index = indexs[number]
    max_number = max_numbers[number]
    index_name = []
    for idx in index:
        # print(idx)
        sql = "select title from policy where number = " + '"' + str(idx) + '"'
        cursor.execute(sql)
        con_engine.commit()
        index_name.append(cursor.fetchall())
    # 开始画图
    nodes = []
    links = []
    categories = []
    context = {'name': name, 'symbolSize': 20, 'draggable': 'False', 'value': number,
               'category': name, 'label': {'normal': {'show:True'}}}
    nodes.append(context)
    for i in range(1, 11):
        context = {'name': index_name[i][0]['title'], 'symbolSize': 10, 'draggable': 'False',
                   'value': int(index[i]),
                   'category': name, 'label': {'normal': {'show:True'}}}
        contexts = {'source': context['category'], 'target': index_name[i][0]['title']}
        nodes.append(context)
        links.append(contexts)
    content = {'name': name}
    categories.append(content)
    data_result = {'nodes': nodes, 'links': links, 'categories': categories}
    jsonArr = json.dumps(data_result, ensure_ascii=False, default=set_default)
    jsonArr = json.dumps(data_result)
    print(type(jsonArr))
    # c = (
    #     Graph()
    #         .add(
    #         "",
    #         nodes,
    #         links,
    #         categories,
    #         repulsion=80,
    #         linestyle_opts=opts.LineStyleOpts(curve=0.2),
    #         label_opts=opts.LabelOpts(is_show=False),
    #     )
    #         .set_global_opts(
    #         legend_opts=opts.LegendOpts(is_show=False),
    #         title_opts=opts.TitleOpts(title="面向企业科技信息服务的可解释推荐系统"),
    #     )
    #         .render("test.html")
    # )
    return data_result


if __name__ == '__main__':
    indexs, max_numbers = top_ten('top_ten.csv')
    json_data = data_json('山西泰通盛矿山机电设备有限公司', indexs, max_numbers)
