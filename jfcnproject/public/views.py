from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Navigation, SiteNavigation, MonitorPlatform
import logging


logger = logging.getLogger('django')


def checkuser(request):
    logger.info("进入用户登陆视图")
    login_info_list = {'info': ''}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info('开始登陆系统，用户名:[%s] 密码:[%s] ' % (username, password))
        # 验证用户是否存在
        try:
            User.objects.get(username=username).password
        except Exception as e:
            logger.info('用户不存在: [%s] 请联系管理员或重新登陆,异常具体原因: %s' % (username, e))
            messages.add_message(request, messages.INFO, '用户不存在')
            login_info_list = {'info': '请使用合法用户登陆或联系管理员处理'}
            return render(request, 'login.html', {'login_info_list': login_info_list})
        # 验证用户密码
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                logger.info('登陆成功,用户名:[%s] 跳转到到系统首页' % username)
                # 把获取表单的用户名传递给session对象
                request.session['username'] = username
                # 设置session过期时间
                request.session.set_expiry(600)
                # return render(request, 'public/index.html')
                return redirect('/public/index/')
        else:
            logger.info('登陆失败,用户:[%s] 用户名或密码错误' % username)
            messages.add_message(request, messages.WARNING, '密码错误')
            login_info_list = {'info': '用户名或密码错误，请重新登陆'}
            return render(request, 'login.html', {'login_info_list': login_info_list})
    else:
        logoutuser = request.GET.get('logoutuser')
        if logoutuser:
            logger.info('退出登陆,用户名:[%s]' % logoutuser)
            logout(request)
            login_info_list = {'info': '退出成功'}
        else:
            logger.info('用户未登陆，跳转至登陆界面')
        return render(request, 'login.html', {"login_info_list": login_info_list})


# @login_required
def siteindex(request):
    logger.info("进入站点导航视图")
    logger.info("获取站点导航数据开始")
    option = request.GET.get('option', None)
    logger.info("站点导航，开始查询[%s]系统导航数据" % option)
    try:
        site_nav = SiteNavigation.objects.all()
        logger.info("获取站点导航数据结束")
    except Exception as e:
        logger.error("获取站点导航数据发生异常,异常原因: %s" % e)
        site_nav = ['获取站点导航数据发生异常,请联系管理员']
    logger.info("返回站点导航数据成功")
    if option == "xx":
        logger.info("进入站点导航查询xx系统")
    elif option == "yy":
        logger.info("进入站点导航查询yy系统")
    return render(request, 'public/url_index.html', {'site_nav_list': site_nav})


def indexpage(request):
    logger.info("进入网站首页")
    logger.info("返回首页数据")
    return render(request, 'public/index.html')





