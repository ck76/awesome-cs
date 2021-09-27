number = [1, 2, 3, 4, 5]
mixL = [1, 'c', "k", 3.14, True, [1, 2, 3]]
mixL.append(False)
print(mixL)

# 使用一个列表来扩展另一个列表
number.extend([6, 7, 8])
print(number)

# 插队
number.insert(1, "insert")
print(number)

# 获取元素
print(mixL[2] + mixL[1])

# 删除元素
# remove() pop() del是一个语句
name = ["鹅蛋", "鸡蛋", "狗蛋", "倒数第二个", "最后一个"]
name.pop(name.__len__() - 2)
print(name)
name.pop()
print(name)
del name[0]
print(name)
# name.remove("程鸡蛋")  报错
name.remove("鸡蛋")
print(name)

# 列表分片[也可以试用步长]
name = ["鹅蛋", "鸡蛋", "狗蛋", "倒数第二个", "最后一个"]
slice = name[:]
print(slice)
slice = name[1:]
print(slice)
slice = name[:3]
print(slice)
slice = name[1:3]  # 左开右闭区间
print(slice)

# y一些常用操作符
list1 = [123]
list2 = [234]
print(list1 > list2)

list3 = ['abc']
list4 = ['bcd']
print(list3 > list4)

# print(list1 > list3) 不能互相比较

list1 = [123, 789]
list2 = [234, 456]
print(list1 > list2)

list3 = ['abc', 'zzz']
list4 = ['bcd', 'bbb']
print(list3 > list4)
# 当列表元素长度不为1的时候，从前往后比，前面的赢了就整体赢了，字符串也是如此

list = [1, 2, 3]
list*=3
print(list )


print(dir(list))
