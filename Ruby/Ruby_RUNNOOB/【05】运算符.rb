
# **	指数 - 执行指数计算	a**b 将得到 10 的 20 次方
#
#
# .eql?	如果接收器和参数具有相同的类型和相等的【值】，则返回 true。	1 == 1.0 返回 true，但是 1.eql?(1.0) 返回 false。
# equal?	如果接收器和参数具有相同的【对象 id】，则返回 true。	如果 aObj 是 bObj 的副本，那么 aObj == bObj 返回 true，a.equal?bObj 返回 false，但是 a.equal?aObj 返回 true。
#
#
# Ruby 范围运算符
# ..	创建一个从开始点到结束点的范围（包含结束点）	1..10 创建从 1 到 10 的范围
# ...	创建一个从开始点到结束点的范围（不包含结束点）	1...10 创建从 1 到 9 的范围

# TODO Ruby defined? 运算符
# defined? 是一个特殊的运算符，以方法调用的形式来判断传递的表达式【是否已定义】。它返回表达式的描述字符串，如果表达式未定义则返回 nil。
# 下面是 defined? 运算符的各种用法：
puts defined? variable # 如果 variable 已经初始化，则为 True
puts foo = 42
puts defined? foo    # => "local-variable"
puts defined? $_     # => "global-variable"
puts defined? bar    # => nil（未定义）

# TODO Ruby 点运算符 "." 和双冒号运算符 "::"
# 你可以通过在方法名称前加上类或模块名称和 . 来调用类或模块中的【方法】。你可以使用【类或模块名称】和两个冒号 :: 来引用类或模块中的【常量】。
# :: 是一元运算符，允许在类或模块内定义常量、实例方法和类方法，可以从类或模块外的任何地方进行访问。
# 请记住：在 Ruby 中，类和方法也可以被当作常量。
# 你只需要在表达式的常量名前加上 :: 前缀，即可返回适当的类或模块对象。
# 如果 :: 前的表达式为类或模块名称，则返回该类或模块内对应的常量值；如果 :: 前未没有前缀表达式，则返回主Object类中对应的常量值。
MR_COUNT = 0        # 定义在主 Object 类上的常量
module Foo
  MR_COUNT = 0
  ::MR_COUNT = 1    # 设置全局计数为 1
  MR_COUNT = 2      # 设置局部计数为 2
end
puts MR_COUNT       # 这是全局常量
puts Foo::MR_COUNT  # 这是 "Foo" 的局部常量

puts "----------------------------------------"

CONST = ' out there'
class Inside_one
  CONST = proc {' in there'}
  def where_is_my_CONST
    ::CONST + ' inside one'
  end
end
class Inside_two
  CONST = ' inside two'
  def where_is_my_CONST
    CONST
  end
end
puts Inside_one.new.where_is_my_CONST
puts Inside_two.new.where_is_my_CONST
puts Object::CONST + Inside_two::CONST
puts Inside_two::CONST + CONST
puts Inside_one::CONST
puts Inside_one::CONST.call + Inside_two::CONST
