# -*- coding: utf-8 -*-

from django.http import HttpResponse
# from TestModel.models import Test
# 数据库操作
# from HelloWorld.TestModel.models import Test
# from HelloWorld.TestModel1.models import Test
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # name 'Test' is not defined
    list = Test.objects.all()

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")