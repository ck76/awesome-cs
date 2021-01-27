from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def runoob(request):
    name = request.GET.get("name")
    return HttpResponse('姓名：{}'.format(name))

@csrf_exempt
# 当采用客户端象 django 的服务器提交 post 请求时，会得到403，权限异常。
# 因为 django 针对提交的请求，有校验。所以会如此。
# 客户端提交的 post 如果不加这段，会出现 403 error
def runoob(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))

def runoob(request):
    name = request.body
    print(name)
    return HttpResponse("菜鸟教程")

def runoob(request):
    name = request.path
    print(name)
    return HttpResponse("菜鸟教程")

def runoob(request):
    name = request.method
    print(name)
    return HttpResponse("菜鸟教程")

def runoob(request):
    # return HttpResponse("菜鸟教程")
    return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")

def runoob(request):
    return redirect("/index/")

