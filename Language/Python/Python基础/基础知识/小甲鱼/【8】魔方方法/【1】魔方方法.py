class Person:
    # 默认打印对象，显示类名+地址
    # 重写该方法，打印该方法的返回值
    def __str__(self):
        return '我叫{}，今年{}岁'.format(self.name, self.age)


james = Person()
james.name = '勒布朗.詹姆斯'
james.age = 33
print(james)  # 我叫勒布朗.詹姆斯，今年33岁


class Cat:
    def __str__(self):
        return 'name:{},age:{},color:{}'.format(self.name, self.age, self.color)

    # 构造方法：创建对象后，会自动调用该方法完成初始化设置
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


jiafei = Cat('加菲', 2, '橘黄色')
print(jiafei)


class Pig:
    # 析构方法：当对象释放时，系统会自动调用
    # 若手动使用del删除，则会立即调用该方法
    # 该方法一般做资源释放操作，如：数据库断开连接，文件关闭
    def __del__(self):
        print('当对象释放时， 系统会自动调用')


bajie = Pig()
del bajie
print('八戒，一路走好')


class Person:
    def __str__(self):
        return '姓名:{}'.format(self.name)

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('对象即将销毁')

    # 当访问不存在的属性时会自动触发该方法
    def __getattr__(self, item):
        if item == 'age':
            return 18
        else:
            return '你猜'

    # 设置属性时会自动触发该方法
    def __setattr__(self, key, value):
        # print(key, value)
        self.__dict__[key] = value

    # 销毁对象的指定属性时会自动触发
    def __delattr__(self, item):
        print(item, '属性即将销毁')


xiaoming = Person('小明')
# print(xiaoming.age)
# print(xiaoming.weight)
#

xiaoming.age = 20
# 存放了所有的对象属性
# print(xiaoming.__dict__)

# print(xiaoming.age)

del xiaoming.age


class Person:
    # 将对象当做字典操作，添加或设置属性时自动触发
    def __setitem__(self, key, value):
        print(key, value)
        self.__dict__[key] = value

    # 将对象当做字典操作，获取属性时自动触发
    def __getitem__(self, item):
        # print(item)
        return self.__dict__.get(item)

    # 将对象当作字典操作，销毁属性时自动触发
    def __delitem__(self, key):
        print(key, '即将销毁')
        del self.__dict__[key]


xiaoming = Person()

xiaoming['name'] = '小明'
# print(xiaoming.name)
print(xiaoming['name'])

del xiaoming['name']


class Person:
    # 将对象当做函数调用时，会自动触发该方法
    def __call__(self, *args, **kwargs):
        # print('__call__', args)
        return sum(args)


xiaoming = Person()
# 如果想这样调用，必须重写__call__方法
ret = xiaoming(1, 2, 3)
print(ret)


def test():
    pass


# 判断一个对象能否被调用
print(callable(xiaoming))
print(callable(test))

# 判断一个对象是否拥有__call__属性
print(hasattr(test, '__call__'))
print(hasattr(xiaoming, '__call__'))

# 判断一个对象是否能够调用
from inspect import isfunction

print(isfunction(test))
print(isfunction(xiaoming))

