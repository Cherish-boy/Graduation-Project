import json
import linecache

import pymysql
from django.http import HttpResponse
from django.shortcuts import render

con_engine = pymysql.connect(host='8.142.138.101',
                             user="root",
                             password='3QB7UkM6xhRTXquz',
                             database="database",
                             port=3306,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

# 使用cursor()方法获取游标
cursor = con_engine.cursor()


def index(request):
    return render(request, '首页.html')


def sign(request):
    return render(request, 'sign.html')


def change(request):
    return render(request, 'change.html')


def form(request):
    # search = request.GET.get('s')
    # print(search)
    # data_dicts = []
    # data = Jincheng.objects.filter(title__icontains=search).values()
    # return render(request, 'search.html', {'i': search, 'n': data})
    return render(request, 'search.html')


def form2(request):
    # search = request.GET.get('s')
    # print(search)
    # data_dicts = []
    # data = Jincheng.objects.filter(title__icontains=search).values()
    # return render(request, 'search.html', {'i': search, 'n': data})
    return render(request, 'test2.html')


def form3(request):
    # search = request.GET.get('s')
    # print(search)
    # data_dicts = []
    # data = Jincheng.objects.filter(title__icontains=search).values()
    # return render(request, 'search.html', {'i': search, 'n': data})
    return render(request, '搜索界面3.html')


def muban(request):
    return render(request, 'muban.html')


def xiangqing(request):
    return render(request, '详细内容.html')


def register(request):
    return render(request, 'register.html')


def company(request):
    return render(request, '公司.html')


def search_name(self):
    # data = request.GET.get('data')
    sql = 'select distinct name,industry,scope from company order by regis_time desc limit 10 '
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print (type(result[0]))
    # print(result[0])
    # print(result)
    # print(result)
    # print(type(result[4]))
    return HttpResponse(json.dumps(result))
    # return JsonResponse(dict(result))


def search_policy(request):
    policy = request.GET.get('policy', None)
    sql = 'select title,release_time,release_source,key_words,abstract,details,prefecture_city from policy where title = ' + '"' + policy + '"'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    return HttpResponse(json.dumps(result[0]))


# 优化了查询速度，展示20条查询结果
def kw_company(request):
    kw = request.GET.get('kw', None)
    kws = kw.split()  # 输入多个关键词以空格隔开，kws为列表
    # print(kws)
    length = len(kws)
    if length == 1:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + 'limit 20'
        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 2:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            1] + "%'" + 'limit 20'
        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 3:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            1] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            2] + "%'" + 'limit 20'
        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 4:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            1] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            2] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            3] + "%'" + 'limit 20'
        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 5:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            1] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            2] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            3] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            4] + "%'" + 'limit 20'
        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 6:
        sql = 'select * from company where concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            0] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            1] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            2] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            3] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            4] + "%'" + \
            'and concat(name,legal_person,address,phone,scope,industry) like ' + "'%" + kws[
            5] + "%'" + 'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))


def search_industry(request):
    indust = request.GET.get('industry', None)
    print(indust)
    sql = 'select * from company where industry = ' + '"' + indust + '"' + 'order by rand() limit 20'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print (type(result[0]))
    print(result)
    # return HttpResponse(json.dumps(result[0]))
    return HttpResponse(json.dumps(result))


def search_title(self):
    sql = 'select title,release_source,abstract from policy order by release_time desc limit 20 '
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print (type(result[0]))
    # print(result[0])
    # print(result)
    # print(result)
    # return HttpResponse(json.dumps(result[0]))
    return HttpResponse(json.dumps(result))


# 查询公司详情界面
def search_company(request):
    com = request.GET.get('company', None)
    sql = 'select * from company where name = ' + '"' + com + '"'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print(result[0])
    return HttpResponse(json.dumps(result[0]))


# 随机查询10条数据
# 查询最热政策，返回所有字段，前端使用时选择
def search_hotpolicy(self):
    sql = 'select * from policy order by rand() limit 20'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print(result[0])
    # print(result)
    return HttpResponse(json.dumps(result))


# 随机查询10条数据
# 查询最热企业，返回所有字段，前端使用时选择
# 查询最热企业
def search_hotcompany(self):
    sql = 'select * from company order by rand() limit 40'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print (type(result[0]))
    # print(result)
    # result为元组带下标，其中每一个元素为json对象
    # return HttpResponse(json.dumps(result[0]))
    result = result[25:35]
    return HttpResponse(json.dumps(result))


def search_newpolicy(self):
    sql = 'select * from policy limit 30'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print (type(result[0]))
    # print(result)
    # result为元组带下标，其中每一个元素为json对象
    # return HttpResponse(json.dumps(result[0]))
    result = result[15:25]
    return HttpResponse(json.dumps(result))



# 查询带有关键字的政策（最多支持6个关键词搜索）
# 前端搜索框初始化显示“请输入关键词，多个关键词请用空格隔开”
# 在字段title,department,release_source,prefecture_city,key_words中查询
def kw_policy(request):
    kw = request.GET.get('kw', None)
    kws = kw.split()
    length = len(kws)

    if length == 1:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + 'order by rand()' + \
              'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 2:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  1] + "%'" + 'order by rand()'+ 'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 3:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  1] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  2] + "%'" + 'order by rand()'+ 'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 4:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  1] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  2] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  3] + "%'" + 'order by rand()'+ 'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 5:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  1] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  2] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  3] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  4] + "%'" +  'order by rand()'+'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))

    if length == 6:
        sql = 'select * from policy where concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + \
              kws[0] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  1] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  2] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  3] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  4] + "%'" + \
              'and concat(title,department,release_source,prefecture_city,details,key_words) like ' + "'%" + kws[
                  5] + "%'" + 'order by rand()'+ 'limit 20'

        # print(sql)
        cursor.execute(sql)
        con_engine.commit()
        result = cursor.fetchall()
        # print(result)
        return HttpResponse(json.dumps(result))





# 给企业推荐政策
# 结果数据为result.csv文件，目前只完成了编号1~9的企业推荐，查询结果展示随机
def recom_policy(request):
    name = request.GET.get('name', None)
    sql = 'select number from company where name =' + '"' + name + '"'
    cursor.execute(sql)
    con_engine.commit()
    number = cursor.fetchall()  # 获取所查询企业的编号
    # print(type(number))    #list型
    # print(type(number[0]))   #dict型
    # print(number[0]['number'])  #拿到企业的编号

    num = number[0]['number']
    # print(num)
    line = linecache.getline("D:/毕设/djangoProject/demo/new_top_ten.csv", num + 1)
    # print(line)
    list1 = line.split(",")
    # print(list1)

    min_index = [index for index, value in sorted(list(enumerate(list1)), key=lambda x: x[1])]  # 政策编号倒序列表
    # print(min_index)
    max_index = list(reversed(min_index))
    # print(max_index)  # max_index为得分最高的政策的number排序列表 max_index[1]为第1政策number为max_index[1]-1，共10个政策，最后一个政策number为max_index[10]-1

    sql = sql = 'select * from policy where number = ' + str(max_index[1] - 1) + ' or ' + 'number = ' + str(
        max_index[2] - 1) + ' or ' + 'number = ' + str(max_index[3] - 1) + \
                ' or ' + 'number = ' + str(max_index[4] - 1) + ' or ' + 'number = ' + str(
        max_index[5] - 1) + ' or ' + 'number = ' + str(max_index[6] - 1) + \
        ' or ' + 'number = ' + str(max_index[7] - 1) + ' or ' + 'number = ' + str(max_index[8] - 1) + \
        ' or ' + 'number = ' + str(max_index[9] - 1) + ' or ' + 'number = ' + str(max_index[10] - 1)

    # print(sql)
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    # print(result)

    return HttpResponse(json.dumps(result))


# 政策详情页面相似政策
# 政策发行部门相同或者发布来源相同
def sim_policy(request):
    title = request.GET.get('title', None)
    print(title)
    sql = 'select department , release_source from policy where title = ' + '"' + title + '"'
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    print(result)
    # 获取目标政策的发行部门和发布来源
    depart = result[0]['department']
    # print(depart)
    source = result[0]['release_source']
    # print(source)
    # 查找与目标政策相似的政策信息,随机展示10条
    sql = 'select * from policy where department = ' + '"' + depart + '"' + 'or release_source = ' + '"' + source + '"' + 'limit 11'
    cursor.execute(sql)
    con_engine.commit()
    results = cursor.fetchall()
    # print(results)
    # 查询结果删除目标政策
    del results[0]
    return HttpResponse(json.dumps(results))


# 用户登录
def logins(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    print(username, password)
    user_tup = {'username': username,
                'password': sha256(password)
                }
    # print(user_tup)
    sql = 'select * from user'
    cursor.execute(sql)
    all_users = cursor.fetchall()
    # print(all_users)
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i = i + 1
    if has_user == 1:
        re = {'1':1}
        return HttpResponse(json.dumps(re))

    else:
        re = {'0':0}
        return HttpResponse(json.dumps(re))

class SHA256:
    def __init__(self):
        #64个常量
        #图中Kt
        self.constants = (
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
            0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
            0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
            0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
            0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
            0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
            0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
            0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
            0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2)
        #迭代初始值，h0,h1,...,h7
        self.h = (
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19)

    #x循环右移b个bit
    #rightrotate b bit
    def rightrotate(self, x, b):
        return ((x >> b) | (x << (32 - b))) & ((2**32)-1)

    #信息预处理。附加填充和附加长度值
    def Pad(self, W):
        return bytes(W, "ascii") + b"\x80" + (b"\x00" * ((55 if (len(W) % 64) < 56 else 119) - (len(W) % 64))) + (
            (len(W) << 3).to_bytes(8, "big"))

    def Compress(self, Wt, Kt, A, B, C, D, E, F, G, H):
        return ((H + (self.rightrotate(E, 6) ^ self.rightrotate(E, 11) ^ self.rightrotate(E, 25)) + (
                    (E & F) ^ (~E & G)) + Wt + Kt) + (
                            self.rightrotate(A, 2) ^ self.rightrotate(A, 13) ^ self.rightrotate(A, 22)) + (
                            (A & B) ^ (A & C) ^ (B & C))) & ((2**32)-1), A, B, C, (D + (
                    H + (self.rightrotate(E, 6) ^ self.rightrotate(E, 11) ^ self.rightrotate(E, 25)) + (
                        (E & F) ^ (~E & G)) + Wt + Kt)) & ((2**32)-1), E, F, G

    def hash(self, message):
        message = self.Pad(message)
        digest = list(self.h)

        for i in range(0, len(message), 64):
            S = message[i: i + 64]
            W = [int.from_bytes(S[e: e + 4], "big") for e in range(0, 64, 4)] + ([0] * 48)

            #构造64个word
            for j in range(16, 64):
                W[j] = (W[j - 16] + (
                            self.rightrotate(W[j - 15], 7) ^ self.rightrotate(W[j - 15], 18) ^ (W[j - 15] >> 3)) + W[
                            j - 7] + (self.rightrotate(W[j - 2], 17) ^ self.rightrotate(W[j - 2], 19) ^ (
                            W[j - 2] >> 10))) & ((2**32)-1)

            A, B, C, D, E, F, G, H = digest

            for j in range(64):
                A, B, C, D, E, F, G, H = self.Compress(W[j], self.constants[j], A, B, C, D, E, F, G, H)

        return "".join(format(h, "02x") for h in b"".join(
            d.to_bytes(4, "big") for d in [(x + y) & ((2**32)-1) for x, y in zip(digest, (A, B, C, D, E, F, G, H))]))


def sha256(massage):
    encoder = SHA256()
    print(f"Output: {encoder.hash(massage)}\n")
    return encoder.hash(massage)


# save函数
def registers(request):
    has_regiter = 0  # 记录当前账号是否存在：0，不存在；1，存在
    # 获取前端提交的数据
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    print(username, sha256(password))
    sql = 'select * from user'
    cursor.execute(sql)
    # 查询到的所有数据存放在allusers里
    all_users = cursor.fetchall()
    i = 0
    while len(all_users) > i:
        if username in all_users[i]['username']:
            # 表示该账号存在
            has_regiter = 1
        i = i + 1
    if has_regiter == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into user(username,password) values(%s,%s)'
        cursor.execute(sql2, (username, sha256(password)))
        con_engine.commit()
        print("true")
        re = {'1':1}
        return HttpResponse(json.dumps(re))
    else:
        re = {'0':0}
        print("false")
        return HttpResponse(json.dumps(re))




def must(request):
    sql = "select title from policy where title LIKE '%国家%' limit 5"
    cursor.execute(sql)
    con_engine.commit()
    result = cursor.fetchall()
    print(result)
    return HttpResponse(json.dumps(result))

def company_pic(request):
    return render(request,'公司大图.html')


def policy_pic(request):
    return render(request,'政策大图.html')

def re_relation(request):
    return render(request,'graphsss.html')