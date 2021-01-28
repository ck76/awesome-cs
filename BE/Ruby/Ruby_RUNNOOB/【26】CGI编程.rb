# TODO Ruby CGI 编程
# Ruby 是一门通用的语言，不仅仅是一门应用于WEB开发的语言，但 Ruby 在WEB应用及WEB工具中的开发是最常见的。
#
# 使用Ruby您不仅可以编写自己的SMTP服务器，FTP程序，或Ruby Web服务器，而且还可以使用Ruby进行CGI编程。
#
# 接下来，让我们花点时间来学习Ruby的CGI编辑。
#
# 网页浏览
# 为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：
#
# 1、使用你的浏览器访问URL并连接到HTTP web 服务器。
# 2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
# 3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。
# CGI程序可以是 Ruby 脚本，Python 脚本，PERL 脚本，SHELL 脚本，C 或者 C++ 程序等。
#

# TODO 编写 CGI 脚本
# 最基本的 Ruby CGI 代码如下所示：
#
#!/usr/bin/ruby

puts "Content-type: text/html\n\n"
puts "<html><body>This is a test</body></html>"


# TODO 使用 cgi.rb
# Ruby 可以调用 CGI 库来编写更复杂的CGI脚本。
# 以下代码调用了 CGI 库来创建一个脚本的CGI脚本。
require 'cgi'

cgi = CGI.new
puts cgi.header
puts "<html><body>This is a test</body></html>"

# TODO 表单处理
# 使用CGI库可以通过两种方式获取表单提交（或URL中的参数）的数据， 例如URL：/cgi-bin/test.cgi?FirstName=Zara&LastName=Ali。
#
# 你可以使用 CGI#[] 来直接获取参数FirstName和LastName：

require 'cgi'
cgi = CGI.new
cgi['FirstName'] # =>  ["Zara"]
cgi['LastName']  # =>  ["Ali"]

require 'cgi'
cgi = CGI.new
h = cgi.params  # =>  {"FirstName"=>["Zara"],"LastName"=>["Ali"]}
h['FirstName']  # =>  ["Zara"]
h['LastName']   # =>  ["Ali"]

require 'cgi'
cgi = CGI.new
cgi.keys         # =>  ["FirstName", "LastName"]

# <html>
# <body>
# <form method="POST" action="http://www.example.com/test.cgi">
# First Name :<input type="text" name="FirstName" value="" />
# <br />
# Last Name :<input type="text" name="LastName" value="" />
#
# <input type="submit" value="Submit Data" />
# </form>
# </body>
# </html>

# TODO 创建 Form 表单和 HTML
# CGI 包含了大量的方法来创建 HTML，每个HTML标签都有相对应的方法。 在使用这些方法前，比必须通过 CGI.new 来创建 CGI 对象。
#
# 为了使标签的嵌套更加的简单，这些方法将内容作为了代码块，代码块将返回字符串作为标签的内容。如下所示：
require "cgi"
cgi = CGI.new("html4")
cgi.out{
  cgi.html{
    cgi.head{ "\n"+cgi.title{"This Is a Test"} } +
        cgi.body{ "\n"+
            cgi.form{"\n"+
                cgi.hr +
                cgi.h1 { "A Form: " } + "\n"+
                cgi.textarea("get_text") +"\n"+
                cgi.br +
                cgi.submit
            }
        }
  }
}


