import os


def read(filename):
    result = []
    file = open(filename, "r")
    for item in file.readlines():
        result.append(item)
    return result

def write2file(path,filename,content):
    open(path+filename)