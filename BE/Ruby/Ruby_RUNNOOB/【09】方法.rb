# TODO Ruby 方法
# Ruby 方法与其他编程语言中的函数类似。Ruby 方法用于捆绑一个或多个重复的语句到一个单元中。
#
# 方法名应以小写字母开头。如果您以大写字母作为方法名的开头，Ruby 可能会把它当作常量，从而导致不正确地解析调用。
#
# 方法应在调用之前定义，否则 Ruby 会产生未定义的方法调用异常。
#
# 语法
# def method_name [( [arg [= default]]...[, * arg [, &expr ]])]
#    expr..
# end

# TODO 参数
def test(a1 = "Ruby", a2 = "Perl")
  puts "编程语言为 #{a1}"
  puts "编程语言为 #{a2}"
end

test "C", "C++"
test


# TODO 返回值
def test2
  i = 100
  j = 200
  k = 300
  return i, j, k
end

var = test2
puts var

# TODO 可变数量的参数
def sample (*test)
  puts "参数个数为 #{test.length}"
  for i in 0...test.length
    puts "参数值为 #{test[i]}"
  end
end

sample "Zara", "6", "F"
sample "Mac", "36", "M", "MCA"

# TODO 类方法
# 当方法定义在类的外部，方法默认标记为 private。另一方面，如果方法定义在类中的，则默认标记为 public。
#
# 方法默认的可见性和 private 标记可通过模块（Module）的 public 或 private 改变。
#
# 当你想要访问类的方法时，您首先需要实例化类。然后，使用对象，您可以访问类的任何成员。
#
# Ruby 提供了一种不用实例化即可访问方法的方式。让我们看看如何声明并访问类方法：
class Accounts
  def reading_charge
  end

  def Accounts.return_date
  end
end

alias foo bar
alias $MATCH $&

undef bar


# Ruby alias 语句
# 这个语句用于为方法或全局变量起别名。别名不能在方法主体内定义。即使方法被重写，方法的别名也保持方法的当前定义。
#
# 为编号的全局变量（$1, $2,...）起别名是被禁止的。重写内置的全局变量可能会导致严重的问题。

# Ruby undef 语句
# 这个语句用于取消方法定义。undef 不能出现在方法主体内。
#
# 通过使用 undef 和 alias，类的接口可以从父类独立修改，但请注意，在自身内部方法调用时，它可能会破坏程序。
