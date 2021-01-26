import urllib.request

print("downloading with urllib")
url = 'http://ds.addsxz.com/123ddtp.pdf'
f = urllib.request.urlopen(url)
data = f.read()
# 存储位置可自定义
with open("sss.pdf", 'wb') as code:
    code.write(data)