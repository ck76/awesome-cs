i = 0
file = open("ck.txt")

result = open("result.txt", mode='w')
for line in file.readlines():
    result.write("inst_mem[" + str(i) + "]= 32'h" + line.replace('\n', '') + ";" + '\n')
    i = i + 1
