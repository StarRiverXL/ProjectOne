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
    url(r'^login_replase_code/$', views.replase_code, name='login_replase_code'),    # 用户登陆ajax验证
    url(r'^login_ajax/$', views.login_ajax, name='login_ajax'),    # 用户登陆刷新验证码
    url(r'^urlindex/$', views.siteindex, name='urlindex'),     # 站点导航
    url(r'^index/$', views.indexpage, name='index'),     # 访问首页
]
