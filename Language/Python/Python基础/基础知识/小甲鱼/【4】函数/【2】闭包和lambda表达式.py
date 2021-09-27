# TODO global关键字修改全局变量
# 在函数内部进进去访问局部变量就好，不要试图去修改他，
# 因为pathon会使用屏蔽（shadowing）的方式保护全局变量
# 相当于拷贝一份

count = 10
globalCount = 10


def changCount():
    count = 20
    global globalCount
    globalCount = 20
    print("count:" + str(count))
    print("globalCount:" + str(globalCount))


changCount()

print("count:" + str(count))
print("globalCount:" + str(globalCount))


# TODO 内嵌函数
def fun1():
    print("fun1调用")

    def fun2():
        print("fun2调用")

    fun2()
    return None


fun1()


# TODO  闭包 closure
def funX(x):
    def funY(y):
        def funZ(z, kkk):
            return x + y + z + kkk

        return funZ

    return funY


funy = funX(10)
funz = funy(20)
result = funz(30, 40)
print(result)
print(funX(10)(20)(30, 40))


# TODO 变量引用
def funX():
    x = 5

    def funY():
        # global x  报错
        nonlocal x
        x = x * x
        return x

    return funY


print(funX()())


def funX():
    x = 5
    x = [5]

    def funY():
        # x *= x  报错
        x[0] *= x[0]
        return x[0]

    return funY


print(funX()())

# TODO lambda表达式
var = lambda x: 2 * x + 1
print(var(50))


#  TODO 介绍两个BIF filter(过滤)和map（映射）
def odd(x):
    return x % 2


temp = filter(None, [1, 0, False, True])
print(list(temp))
temp = filter(odd, [1, 0, False, True])
print(list(temp))

print(list(map(lambda x: x * 2, range(10))))