import sys

sys.setrecursionlimit(10000000)  # 将递归限制设置为100万层


# TODO 普通循环求阶乘

def recursion(num):
    result = num
    for i in range(1, num):
        result = result * i
    return result


def recursionX(num):
    if num == 1:
        return 1
    return num * recursionX(num - 1)


print(recursion(50))
print(recursionX(50))


# TODO 斐波那契数列
def feb(num):
    if num == 1 or num == 2:
        return 1
    else:
        return feb(num - 1) + feb(num - 2)


print(feb(10))


# TODO 汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "-->", z)  # 如果只有一层直接x--》z
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        print(x, "-->", z)  # 将最底下的第64个盘子从x移动到z
        hanoi(n - 1, y, x, z)  # 将y上的63个盘子移动到z上


n = int(input("请输入汉诺塔的层数:\n"))
hanoi(n, 'X', 'Y', 'Z')
