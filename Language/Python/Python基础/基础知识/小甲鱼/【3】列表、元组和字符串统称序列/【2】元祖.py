# 元祖和列表最大的区别就是你可以任意修改和添加删除列表中的元素，但是元祖像字符串一样是不可变的
tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple)
singleTuple = (1)
print(type(singleTuple))  # <class 'int'>
print(type(tuple))  # <class 'tuple'>
singleTuple = 1, 2, 3
singleTuple = 1,
singleTuple = ()
print(type(singleTuple))

# 通过分片进行更新和删除元素的操作
# del tuple[1]  错误
del tuple
print(tuple)
