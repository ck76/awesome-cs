import os

dong = ["A5", "A6", "A7", "A8", "A9", "A11", "A13", "A14", "A15", "A16", "A19"]

filepath = "xlss"
filenames = os.listdir(filepath)

count = 0
danyuanshu = 2

for donggg in dong:
    if donggg == "A15" or donggg == "A16":
        danyuanshu = 3
    elif donggg == "A19":
        danyuanshu = 4
    else:
        danyuanshu = 2
    for danyuan in range(danyuanshu):
        for louceng in range(5):
            os.rename(filepath + '/' + filenames[count],
                      filepath + '/' + donggg + "-" + str(danyuan + 1) + "-" + str(louceng + 1) + "01" + ".xlsx")
            count = count + 1
            os.rename(filepath + '/' + filenames[count],
                      filepath + '/' + donggg + "-" + str(danyuan + 1) + "-" + str(louceng + 1) + "02" + ".xlsx")
            count = count + 1
