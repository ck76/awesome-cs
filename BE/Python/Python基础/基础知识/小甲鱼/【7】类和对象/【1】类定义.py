class MyClass:
    """一个简单的实例"""
    i = 12345

    def __init__(self, new):
        # global i
        # i = 45678
        self.i = new

    def __init__(self, new1, new2):
        # global i
        # i = 45678
        self.i = new2

    def hello(self):
        return "hello world"


myclass = MyClass(45678, 56789)
print(myclass.i)
