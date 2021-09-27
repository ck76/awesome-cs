import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

seesion = requests.session()

# 因为人人网有from表单，所以可以直接找地址：http://www.renren.com/PLogin.do
# 如果没有的就要抓包了

post_url = "http://www.renren.com/PLogin.do"    # form表单里面直接找到的
#post_url = "http://www.renren.com/ajaxLogin/login?
# 用户名作为键， 真正的密码作为值  模拟登陆
post_data = {"email":"xxxx", "password":"xxxx"}
seesion.post(post_url, headers = headers, data = post_data)

url = "再次请求登陆的url"

response = seesion.get(url, headers = headers)

with open("renren3.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())