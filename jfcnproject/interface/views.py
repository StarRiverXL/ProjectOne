from django.shortcuts import render, redirect, HttpResponse
import json, simplejson
# Create your views here.
import logging
logger = logging.getLogger('django')

date = {
  "getNewsList": [
    {
      "id": 1,
      "title": "新闻条目1新闻条目1新闻条目1新闻条目1",
      "url": "http://starcraft.com"
    },
    {
      "id": 2,
      "title": "新闻条目2新闻条目2新闻条目2新闻条目2",
      "url": "http://warcraft.com"
    },
    {
      "id": 3,
      "title": "新闻条3新闻条3新闻条3",
      "url": "http://overwatch.com"
    },
    {
      "id": 4,
      "title": "新闻条4广告发布",
      "url": "http://hearstone.com"
    }
  ],
  "login": {
    "username": "yudongdong",
    "userId": 123123
  },
  "getPrice": {
    "amount": 678
  },
  "createOrder": {
    "orderId": "6djk979"
  },
  "getOrderList": {
    "list": [
      {
        "orderId": "ddj123",
        "product": "数据统计",
        "version": "高级版",
        "period": "1年",
        "buyNum": 2,
        "date": "2016-10-10",
        "amount": "500元"
      },
      {
        "orderId": "yuj583",
        "product": "流量分析",
        "version": "户外版",
        "period": "3个月",
        "buyNum": 1,
        "date": "2016-5-2",
        "amount": "2200元"
      },
      {
        "orderId": "pmd201",
        "product": "广告发布",
        "version": "商铺版",
        "period": "3年",
        "buyNum": 12,
        "date": "2016-8-3",
        "amount": "7890元"
      }
    ]
  }
}


def wenming(request):
    # req = {"aa": "c"}
    # return HttpResponse(json.dumps(req))

    # req = simplejson.loads(request.body)
    # return HttpResponse(simplejson.dumps(req))

    key = request.GET.get("key")
    logger.info("接口获取数据,输入参数kew值为：%s" % key)
    value = date.get(key)
    logger.info("接口获取数据成功")
    return HttpResponse(simplejson.dumps(value))



