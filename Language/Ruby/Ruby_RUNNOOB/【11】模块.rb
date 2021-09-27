#TODO Ruby 模块（Module）
# 模块（Module）是一种把方法、类和常量组合在一起的方式。模块（Module）为您提供了两大好处。
#
# 模块提供了一个命名空间和避免名字冲突。
# 模块实现了 mixin 装置。
# 模块（Module）定义了一个命名空间，相当于一个沙盒，在里边您的方法和常量不会与其他地方的方法常量冲突。
#
# 模块类似与类，但有以下不同：
#
# 模块不能实例化
# 模块没有子类
# 模块只能被另一个模块定义
# 语法
# module Identifier
#   statement1
#   statement2
#   ...........
# end

# TODO Ruby require 语句-------------------------------
$LOAD_PATH << '.'

require 'trig.rb'
require 'moral'
require 'support'

y = Trig.sin(Trig::PI / 4)
wrongdoing = Moral.sin(Moral::VERY_BAD)
#  在这里，我们使用 $LOAD_PATH << '.' 让 Ruby 知道必须在当前目录中搜索被引用的文件。如果您不想使用 $LOAD_PATH，那么您可以使用 require_relative 来从一个相对目录引用文件。
# 注意：在这里，文件包含相同的函数名称。所以，这会在引用调用程序时导致代码模糊，但是模块避免了这种代码模糊，而且我们可以使用模块的名称调用适当的函数。


# TODO Ruby include 语句-----------------------------
class Decade
  include Week #代码
  no_of_yrs = 10

  def no_of_months
    puts Week::FIRST_DAY
    number = 10 * 12
    puts number
  end
end
d1 = Decade.new
puts Week::FIRST_DAY
Week.weeks_in_month
Week.weeks_in_year
d1.no_of_months

# Sunday
# You have four weeks in a month
# You have 52 weeks in a year
# Sunday
# 120

# TODO Ruby 中的 Mixins------------------------------------
module A
  def a1
  end
  def a2
  end
end
module B
  def a1 #名字冲突也没事
  end
  def b1
  end
  def b2
  end
end

class Sample
  include A
  include B
  def s1
  end
end

samp=Sample.new
samp.a1
samp.a2
samp.b1
samp.b2
samp.s1
# 模块 A 由方法 a1 和 a2 组成。
# 模块 B 由方法 b1 和 b2 组成。
# 类 Sample 包含了模块 A 和 B。
# 类 Sample 可以访问所有四个方法，即 a1、a2、b1 和 b2。
# 因此，您可以看到类 Sample 继承了两个模块，您可以说类 Sample 使用了多重继承或 mixin 。
