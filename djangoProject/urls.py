"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demo import views
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")### 把test02 改成自己的项目名即可
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.change),
    path('index/sign',views.sign),##登录页面
    path('index/register',views.register),##注册页面
    path('index/首页.html', views.index),
    path('index/search.html', views.form),#三个搜索界面
    path('index/test2.html', views.form2),
    path('index/搜索界面3.html', views.form3),
    path('index/muban', views.muban),
    path('index/详细内容.html', views.xiangqing),
    path('index/公司', views.company),
    path('index/search.html/公司', views.company),
    path('index/api', views.search_policy),
    path('index/newcompany',views.search_name),##最新企业
    path('index/zuixin', views.search_title),
    path('index/gongsi',views.search_company),
    # 新的
    path('index/hotpolicy', views.search_hotpolicy),
    path('index/hotcompany',views.search_hotcompany),
    path('index/newpolicy',views.search_newpolicy),
    path('index/recom',views.recom_policy),##推荐的政策
    path('index/result',views.kw_company),#搜索公司
    path('index/re',views.kw_policy),#搜索政策
    path('index/result3',views.search_industry),#
    path('index/simpolicy',views.sim_policy),##相似政策
    path('index/logins',views.logins),#将登录数据传回后台
    path('index/registers',views.registers),#将注册数据传回后台
    # path('index/ksh',views.ksh),
    path('index/must',views.must),#返回必读政策
    path('index/公司大图.html', views.company_pic),
    path('index/政策大图.html', views.policy_pic),
    path('index/graphesss.html',views.re_relation)
]
