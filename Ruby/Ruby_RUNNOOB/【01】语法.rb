#!/usr/bin/ruby -w

# TODO 声明 code 会在程序运行之前被调用。
BEGIN {
  puts "初始化 Ruby 程序"
}

puts "Hello, Ruby!";

END {
  puts "停止 Ruby 程序"
}
# TODO Ruby 程序中的空白
# 在 Ruby 代码中的空白字符，如空格和制表符一般会被忽略，除非当它们出现在字符串中时才不会被忽略。然而，有时候它们用于解释模棱两可的语句。当启用 -w 选项时，这种解释会产生警告。
# a + b 被解释为 a+b （这是一个局部变量）
# a  +b 被解释为 a(+b) （这是一个方法调用）

# TODO Ruby 程序中的行尾
# Ruby 把分号和换行符解释为语句的结尾。但是，如果 Ruby 在行尾遇到运算符，比如 +、- 或反斜杠，它们表示一个语句的延续。

# TODO Ruby 标识符
# 标识符是变量、常量和方法的名称。Ruby 标识符是大小写敏感的。这意味着 Ram 和 RAM 在 Ruby 中是两个不同的标识符。
# Ruby 标识符的名称可以包含字母、数字和下划线字符（ _ ）。

# TODO 保留字
# 下表列出了 Ruby 中的保留字。这些保留字不能作为常量或变量的名称。但是，它们可以作为方法名。
# BEGIN	do	next	then
# END	else	nil	true
# alias	elsif	not	undef
# and	end	or	unless
# begin	ensure	redo	until
# break	false	rescue	when
# case	for	retry	while
# class	if	return	while
# def	in	self	__FILE__
# defined?	module	super	__LINE__

#TODO Ruby 中的 Here Document
# "Here Document" 是指建立多行字符串。在 << 之后，您可以指定一个字符串或标识符来终止字符串，且当前行之后直到终止符为止的所有行是字符串的值。
# 如果终止符用引号括起，引号的类型决定了面向行的字符串类型。请注意<< 和终止符之间必须没有空格。
print <<EOF
    这是第一种方式创建here document 。
    多行字符串。
EOF

print <<"EOF";                # 与上面相同
    这是第二种方式创建here document 。
    多行字符串。
EOF

print <<`EOC`                 # 执行命令
    echo hi there
    echo lo there
EOC

print <<"foo", <<"bar"          # 您可以把它们进行堆叠
    I said foo.
foo
    I said bar.
bar

# Hello, Ruby!
#     这是第一种方式创建here document 。
#     多行字符串。
#     这是第二种方式创建here document 。
#     多行字符串。
# hi there
# lo there
#     I said foo.
#     I said bar.


# TODO Ruby 注释
=begin
这是注释。
这也是注释。
这也是注释。
这还是注释。
=end
