#coding=cp936

import matplotlib.pyplot as plt

import numpy as np
# TODO osaka
shouyan_science = [28, 28, 23, 30, 25]
shouyan_system = [23, 26, 30, 20, 30, ]
shouyan_network = [19, 29, 21, 22, 34]
shouyan_maruchimediae = [30, 23, 33, 34, 38, ]
shouyan_baio = [20, 23, 30, 24, 26, ]
shouyan_sum = [152, 154, 175, 163, 192, ]

hege_science = [26, 23, 24, 23, 24]
hege_system = [23, 23, 24, 24, 26, ]
hege_network = [22, 21, 22, 23, 24]
hege_maruchimediae = [24, 24, 23, 22, 28, ]
hege_baio = [19, 21, 19, 21, 22, ]
hege_sum = [143, 133, 146, 138, 152, ]

beilv_science = []
beilv_system = []
beilv_network = []
beilv_maruchimediae = []
beilv_baio = []
beilv_sum = []
percent_science = []
percent_system = []
percent_network = []
percent_maruchimediae = []
percent_baio = []
percent_sum = []
# print(shouyan_sum[0]/hege_sum[0])
for i in range(0, len(shouyan_sum)):
    item_beilv_science = shouyan_science[i] / hege_science[i]
    beilv_science.append(item_beilv_science)
    item_percent_science = hege_science[i] / shouyan_science[i]
    percent_science.append(item_percent_science)

    item_beilv_system = shouyan_system[i] / hege_system[i]
    beilv_system.append(item_beilv_system)
    item_percent_system = hege_system[i] / shouyan_system[i]
    percent_system.append(item_percent_system)

    item_beilv_network = shouyan_network[i] / hege_network[i]
    beilv_network.append(item_beilv_network)
    item_percent_network = hege_network[i] / shouyan_network[i]
    percent_network.append(item_percent_network)

    item_beilv_maruchimediae = shouyan_maruchimediae[i] / hege_maruchimediae[i]
    beilv_maruchimediae.append(item_beilv_maruchimediae)
    item_percent_maruchimediae = hege_maruchimediae[i] / shouyan_maruchimediae[i]
    percent_maruchimediae.append(item_percent_maruchimediae)

    item_beilv_baio = shouyan_baio[i] / hege_baio[i]
    beilv_baio.append(item_beilv_baio)
    item_percent_baio = hege_baio[i] / shouyan_baio[i]
    percent_baio.append(item_percent_baio)

    item_beilv_sum = shouyan_sum[i] / hege_sum[i]
    beilv_sum.append(item_beilv_sum)
    item_percent_sum = hege_sum[i] / shouyan_sum[i]
    percent_sum.append(item_percent_sum)

print(beilv_science)
print(beilv_system)
print(beilv_network)
print(beilv_maruchimediae)
print(beilv_baio)
print(beilv_sum)

nian = [16, 17, 18, 19, 20]

y = beilv_sum
x = nian

x = np.linspace(16, 20, 5)
plt.figure(figsize=(1, 2))
# 一个窗口，多个图，多条数据
sub1 = plt.subplot(211, )  # 将窗口分成2行1列，在第1个作图，并设置背景色
sub2 = plt.subplot(212)  # 将窗口分成2行1列，在第2个作图
sub1.plot(x, beilv_science, label="1")  # 绘制子图
sub1.plot(x, beilv_system, label="2")
sub1.plot(x, beilv_network, label="3")
sub1.plot(x, beilv_maruchimediae, label="4")
sub1.plot(x, beilv_baio, label="5")
sub1.plot(x, beilv_sum, label="6")
sub2.plot(x, percent_science, label="1")  # 绘制子图
sub2.plot(x, percent_system, label="2")
sub2.plot(x, percent_network, label="3")
sub2.plot(x, percent_maruchimediae, label="4")
sub2.plot(x, percent_baio, label="5")
sub2.plot(x, percent_sum, label="6")
sub2.legend(loc=0,)
plt.show()
# TODO kyoto
