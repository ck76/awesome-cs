# 整型

# 浮点型
a = 0.0000000000000000000000000000000025
print(a)  ##2.5e-33

# 布尔类型
ckTrue = True + True
ckFalse = False + False
print(ckTrue)  # 2
print(ckFalse)  # 0

# 类型转换
a = '520'
print(int(520.1))  # 直接砍掉，不是四舍五入
print(float(a))
print(str(a))

# 获取有关类型的信息
print(type('520'))
ck = type('520')
print(isinstance('520', float))

