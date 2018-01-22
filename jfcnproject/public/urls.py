#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time ： 
# Email： 
from django.conf.urls import url

from . import views

# 视图函数命名空间
app_name = 'public'
urlpatterns = [
    url(r'^login/$', views.checkuser, name='login'),    # 用户登陆
    url(r'^urlindex/$', views.siteindex, name='urlindex'),     # 站点导航
    url(r'^index/$', views.indexpage, name='index'),     # 访问首页
]
