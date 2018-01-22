from django.test import TestCase

import time
localtime_download = time.strftime("%Y%m%d_%H%M%S", time.localtime())




print("/app/apache-tomcat-7-ss/logs/catalina.out")


# return HttpResponse('<a href="http://127.0.0.1:8000/app02/downloadlog/?download_log_name=catalina_20180103_182024">点我下载日志</a>')

# /app02/downloadlog/?download_log_name=catalina_20180103_182024


# if request.method == "POST":
#     data = {"status": True, "failReason": "验证码错误"}
#     return HttpResponse(json.dumps(data))

#  页面：$("#verify_code_key").val(data.filename);

# elif request.method == 'GET':
# opt = request.GET.get('opt', None)
# ip = request.GET.get('IP', None)
# logger.info("服务器基础操作参数(GET方式)，IP:[%s],操作类型:[%s]" % (ip, opt))
# ip_db_query = get_db_data(tablename=viewlog, ip=ip)
# data = {"status": True, "failReason": "验证码错误"}
# search_messages = ["请选择查询条件a"]
# if ip_db_query.exists():
#     # 通过ip获取连接服务器的只读用户、密码、SSH端口
#     for i in ip_db_query:
#         ip_username = i.username
#         ip_passwd = i.passwd
#         ip_ssh_port = i.SSHport
#         server = ServerOptControl(ip=ip, ip_username=ip_username, ip_passwd=ip_passwd, ip_port=ip_ssh_port)
#     if opt == "4":
#         log_download_path = request.GET.get('log_download_path', None)  # 日志下载路径
#         log_download_begin_line = request.GET.get('log_download_begin_line', None)  # 日志下载路径开始行号
#         log_download_end_line = request.GET.get('log_download_end_line', None)  # 日志下载路径结束行号
#         logger.info("本次操作为：日志下载，操作IP：[{0}],日志下载路径：[{1}],日志下载路径开始、"
#                     "结束行号：[{2}:{3}]".format(ip, log_download_path, log_download_begin_line,
#                                             log_download_end_line))
#         # data = server.log_download_control(log_download_path, log_download_begin_line, log_download_end_line)
#         # if data["safe"]:
#         #     # logger.info("----------调试返回数据----------%s" % data)
#         #     search_messages = data["result"]
#         # else:
#         #     logger.error("日志下载命令执行失败")
#         #     search_messages = ["日志下载命令执行失败，请联系管理员处理。"]
#         data = {"status": True, "failReason": "验证码错误aaa"}
#         return HttpResponse(json.dumps(data))
# return render(request, 'app02/viewlog.html', {"log": search_messages})











