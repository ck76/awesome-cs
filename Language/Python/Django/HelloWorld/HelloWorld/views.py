from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World!")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['ck'] = "ck"
    views_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3", ]
    context["views_list"] = views_list
    views_dict = {"name": "菜鸟教程", "age": 18}
    context['views_dict'] = views_dict
    # 模板语法：
    # view：｛"HTML变量名" : "views变量名"｝
    # HTML：｛｛变量名｝｝

    # 过滤器
    # 模板语法：
    # {{ 变量名 | 过滤器：可选参数 }}
    return render(request, 'runoob.html', context)


def extends(request):
    return HttpResponse(request, "extends.html")

