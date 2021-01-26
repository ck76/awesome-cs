def add(num1, num2):
    return num1 + num2


# 函数文档
def funDoc():
    """
    这是函数文档
    """
    return "ck"
print(funDoc().__doc__)
help(funDoc())


# 关键字参数
def keyWordFun(name, words):
    print(name + words)
keyWordFun(name="ck", words="kakakakkakakakaka")


# 默认参数
def 默认参数(param, name=" ck ", word=" jajaj "):
    print(param + name + word)
默认参数("param", word=" kakakakakkaka ")


# 收集参数---可变参数 ,参数收集上来打包成一个元祖
def test(*params,extra):
    print(params)
    print(extra)

test(1,2,3,4,"ckckckc",extra=" extra")


# 函数和过程
def hello():
    print("hello")
    # return  None默认是这个
print(hello())


