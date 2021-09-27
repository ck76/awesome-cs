#
# TODO 文件读写模式
content = """只读 r
只写
    覆盖 w
    不覆盖 a
读写
    覆盖 w+
    不覆盖
        开头追加 r+
        结尾追加 a+"""

file = open("ck.txt", mode='w+', buffering=-1, encoding='UTF-8', errors=None, newline=None, closefd=True, opener=None)
# 虽然python会垃圾回收不会造成内存泄漏。但是缓泻数据可能导致数据丢失如果不及时关闭文件
file.write(content)
file.close()
file = open("ck.txt")
print(file.readline())
print(file.tell())
# print(file.readlines())
for i in list(file):
    print(i)

file.read()

#  TODO 文件写入 确保读写模式有w 或者a
