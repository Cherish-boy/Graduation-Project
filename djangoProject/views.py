from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.forms.models import model_to_dict
from django.shortcuts import render, HttpResponse, redirect
import pymysql
import json


def index(request):
    # data_dicts_1 = []
    # for i in range(1, 20):
    #     data = Jincheng.objects.filter(id=i).first()
    #     data_dic = {'title': data.title, 'fabu': data.release_source, 'key_words': data.key_words, 'id': data.id}
    #     data_dicts_1.append(data_dic)
    # data_dicts_2 = []
    # for i in range(21, 40):
    #     data = Jincheng.objects.filter(id=i).first()
    #     data_dic = {'title': data.title, 'fabu': data.release_source, 'key_words': data.key_words, 'id': data.id}
    #     data_dicts_2.append(data_dic)

    return render(request, '首页.html')


def form(request):
    # search = request.GET.get('s')
    # print(search)
    # data_dicts = []
    # data = Jincheng.objects.filter(title__icontains=search).values()
    # return render(request, 'search.html', {'i': search, 'n': data})
    return render(request, 'search.html')


def muban(request):
    return render(request, 'muban.html')


def xiangqing(request):
    # ids = request.GET.get('t')
    # print(ids)
    # data = Jincheng.objects.filter(id=ids).first()
    # data_dic = {'title': data.title, 'fabu': data.release_source, 'key_words': data.key_words, 'details': data.details,
    #             'deadline': data.release_time}
    # print(data_dic)
    # return render(request, '详细内容.html', {'n': data_dic})

    return render(request, '详细内容.html')


def company(request):
    return render(request, '公司.html')

