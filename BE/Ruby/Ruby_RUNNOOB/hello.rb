#!/usr/bin/ruby
# !/usr/bin/ruby -w
# -*- coding: UTF-8 -*-
#
puts "你好，世界！"
puts 'Hello World!'

# https://www.runoob.com/ruby/ruby-tutorial.html
#
# Ruby 的特性
# Ruby 是开源的，在 Web 上免费提供，但需要一个许可证。
# Ruby 是一种通用的、解释的编程语言。
# Ruby 是一种真正的面向对象编程语言。
# Ruby 是一种类似于 Python 和 Perl 的服务器端脚本语言。
# Ruby 可以用来编写通用网关接口（CGI）脚本。
# Ruby 可以被嵌入到超文本标记语言（HTML）。
# Ruby 语法简单，这使得新的开发人员能够快速轻松地学习 Ruby。
# Ruby 与 C++ 和 Perl 等许多编程语言有着类似的语法。
# Ruby 可扩展性强，用 Ruby 编写的大程序易于维护。
# Ruby 可用于开发的 Internet 和 Intranet 应用程序。
# Ruby 可以安装在 Windows 和 POSIX 环境中。
# Ruby 支持许多 GUI 工具，比如 Tcl/Tk、GTK 和 OpenGL。
# Ruby 可以很容易地连接到 DB2、MySQL、Oracle 和 Sybase。
# Ruby 有丰富的内置函数，可以直接在 Ruby 脚本中使用。

# TODO Ruby 命令行选项
# 解释器可以通过下列选项被调用，来控制解释器的环境和行为。
#
# 选项	描述
# -a	与 -n 或 -p 一起使用时，可以打开自动拆分模式(auto split mode)。请查看 -n 和 -p 选项。
# -c	只检查语法，不执行程序。
# -C dir	在执行前改变目录（等价于 -X）。
# -d	启用调试模式（等价于 -debug）。
# -F pat	指定 pat 作为默认的分离模式（$;）。
# -e prog	指定 prog 作为程序在命令行中执行。可以指定多个 -e 选项，用来执行多个程序。
# -h	显示命令行选项的一个概览。
# -i [ ext]	把文件内容重写为程序输出。原始文件会被加上扩展名 ext 保存下来。如果未指定 ext，原始文件会被删除。
# -I dir	添加 dir 作为加载库的目录。
# -K [ kcode]	指定多字节字符集编码。e 或 E 对应 EUC（extended Unix code），s 或 S 对应 SJIS（Shift-JIS），u 或 U 对应 UTF-8，a、A、n 或 N 对应 ASCII。
# -l	启用自动行尾处理。从输入行取消一个换行符，并向输出行追加一个换行符。
# -n	把代码放置在一个输入循环中（就像在 while gets; ... end 中一样）。
# -0[ octal]	设置默认的记录分隔符（$/）为八进制。如果未指定 octal 则默认为 \0。
# -p	把代码放置在一个输入循环中。在每次迭代后输出变量 $_ 的值。
# -r lib	使用 require 来加载 lib 作为执行前的库。
# -s	解读程序名称和文件名参数之间的匹配模式 -xxx 的任何参数作为开关，并定义相应的变量。
# -T [level]	设置安全级别，执行不纯度测试（如果未指定 level，则默认值为 1）。
# -v	显示版本，并启用冗余模式。
# -w	启用冗余模式。如果未指定程序文件，则从 STDIN 读取。
# -x [dir]	删除 #!ruby 行之前的文本。如果指定了 dir，则把目录改变为 dir。
# -X dir	在执行前改变目录（等价于 -C）。
# -y	启用解析器调试模式。
# --copyright	显示版权声明。
# --debug	启用调试模式（等价于 -d）。
# --help	显示命令行选项的一个概览（等价于 -h）。
# --version	显示版本。
# --verbose	启用冗余模式（等价于 -v）。设置 $VERBOSE 为 true。
# --yydebug	启用解析器调试模式（等价于 -y）。
# 单字符的命令行选项可以组合使用。下面两行表达了同样的意思：
#
# $ ruby -ne 'print if /Ruby/' /usr/share/bin
#
#
# $ ruby -n -e 'print if /Ruby/' /usr/share/bin

# TODO Ruby 环境变量
#
# 变量	描述
# DLN_LIBRARY_PATH	动态加载模块搜索的路径。
# HOME	当没有参数传递给 Dir::chdir 时，要移动到的目录。也用于 File::expand_path 来扩展 "~"。
# LOGDIR	当没有参数传递给 Dir::chdir 且未设置环境变量 HOME 时，要移动到的目录。
# PATH	执行子进程的搜索路径，以及在指定 -S 选项后，Ruby 程序的搜索路径。每个路径用冒号分隔（在 DOS 和 Windows 中用分号分隔）。
# RUBYLIB	库的搜索路径。每个路径用冒号分隔（在 DOS 和 Windows 中用分号分隔）。
# RUBYLIB_PREFIX	用于修改 RUBYLIB 搜索路径，通过使用格式 path1;path2 或 path1path2，把库的前缀 path1 替换为 path2。
# RUBYOPT	传给 Ruby 解释器的命令行选项。在 taint 模式时被忽略（其中，$SAFE 大于 0）。
# RUBYPATH	指定 -S 选项后，Ruby 程序的搜索路径。优先级高于 PATH。在 taint 模式时被忽略（其中，$SAFE 大于 0）。
# RUBYSHELL	指定执行命令时所使用的 shell。如果未设置该环境变量，则使用 SHELL 或 COMSPEC。
