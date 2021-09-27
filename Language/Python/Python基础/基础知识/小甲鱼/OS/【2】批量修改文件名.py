# python 对文件进行批量改名用到的是 os 模块中的 listdir 方法和 rename 方法。
#
#  os.listdir(dir) : 获取指定目录下的所有子目录和文件名
#  os.rename(原文件名，新文件名） : 对文件或目录改名
# 把混乱的文件名改成有序的文件名:
import os

path = input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

n = 0
for i in fileList:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = path + + os.sep + 'a' + str(n + 1) + '.JPG'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1
