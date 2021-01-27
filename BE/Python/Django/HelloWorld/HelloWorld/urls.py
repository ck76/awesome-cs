
from django.contrib import admin
from django.urls import path

from . import views, testdb

# path() 函数
# Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。
# 语法格式：
# path(route, view, kwargs=None, name=None)
# route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
# view: 用于执行与正则表达式匹配的 URL 请求。
# kwargs: 视图使用的字典类型的参数。
# name: 用来反向获取 URL。


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('runoob/', views.runoob),
    path('entends/', views.extends),
    path('testdb/', testdb.testdb),

]
