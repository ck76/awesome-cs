# 条件分支
import random

secret = random.randint(1, 10)
print("secret=" + secret.__str__())
guess = 0
while guess != secret:
    temp = input("猜错了，请重新输入")
    guess = int(temp)
    if guess == secret:
        print("猜对了")
    elif guess > secret:
        print("猜大了")
    else:
        print("猜小了")