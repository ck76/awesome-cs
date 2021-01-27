# _*_ coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

# #数据库操作
# def testdb(request):
#     test1 = Test(name='kq')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")
# #数据库操作
# def testdb(request):
#     #初始化
#     response = ""
#     response1 =""
#
#     #通过objects 模型管理器的all() 获取所有数据
#     list = Test.objects.all()
#
#     #filter设置条件过滤，相当于where
#     response2 = Test.objects.filter(id=1)
#
#     #获取单个对象
#     response3 = Test.objects.get(id=1)
#
#     #限制返回数据 相当于 OFFSET 0 LIMIT 2
#     Test.objects.order_by('name')[0:2]
#
#     #数据库排序
#     Test.objects.order_by("id")
#
#     # 连锁使用
#     Test.objects.filter(name="kq").order_by("id")
#
#     for var in list:
#         response1 += var.name + ""
#     response=response1
#     return HttpResponse("<p>"+ response +"</p>")

# #更新数据
# def testdb(request):
#     # 修改其中一个id=1 再保存 相当于update
#     test1 = Test.objects.get(id=1)
#     test1.name ="Google"
#     test1.save()
#
#     return HttpResponse("<p>修改成功</p>")
# 数据库操作
def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")