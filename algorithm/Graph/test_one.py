import pymysql

from top_10 import top_ten

con_engine = pymysql.connect(host='8.142.138.101',
                                 user="root",
                                 password="0552fe7ad2067bda",
                                 database="database",
                                 port=3306,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
cursor = con_engine.cursor()
name = '山西泰通盛矿山机电设备有限公司'
sql = "select number from company where name = " + '"' + name + '"'
cursor.execute(sql)
con_engine.commit()
result = cursor.fetchall()
number = result[0]['number']
indexs, max_numbers = top_ten('../top_ten.csv')
index = indexs[number]
max_number = max_numbers[number]
index_name = []
for idx in index:
    print(idx)
    sql = "select title from policy where number = " + '"' + str(idx) + '"'
    cursor.execute(sql)
    con_engine.commit()
    index_name.append(cursor.fetchall())
print(index_name[1])
# 开始画图
# nodes = []
# links = []
# categories = []
# context = {'name': name, 'symbolSize': 20, 'draggable': 'False', 'value': name,
#                'category': name, 'label': {'normal': {'show:True'}}}
# nodes.append(context)
# for i in range(1,11):
#     context = {'name': name, 'symbolSize': 20, 'draggable': 'False', 'value': name,
#                    'category': name, 'label': {'normal': {'show:True'}}}
