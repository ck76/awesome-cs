# TODO
import sys

#  TODO 手动抛出异常
try:
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
except:
    print('x 不能大于 5')

try:
    file = open("ck.txt")  # FileNotFoundError
    for line in file.readlines():
        print(line)
except OSError:
    print("该文件不存在")

# TODO 1 assertionexception
try:
    my_list = ['ck']
    assert len(my_list) > 0
    my_list.pop()
    assert len(my_list) > 0
except AssertionError:
    print("asserterror")

# TODO 访问的对象属性不存在
try:
    print(my_list.ck)
except AttributeError:
    print('访问的对象属性不存在')

# TODO 索引超出范围
try:
    my_list[100]
except IndexError:
    print("索引超出范围")

# TODO 字典中查找一个不存在的关键字
try:
    my_dict = {"one": 1, "two": 2}
    my_dict["three"]
except KeyError:
    print("字典中查找一个不存在的关键字")

# TODO 反正还有很多Error

# TODO 针对不同异常设置多个except
try:
    sum = 1 + '1'
    file = open("ck.txt")
    print(file.read())
    file.close()
except OSError as reason:
    print("文件出错原因是：" + str(reason))
except TypeError as reason:
    print("类型出错 原因是：" + str(reason))

# TODO 对多个异常统一处理
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

