# TODO Ruby 块
# 您已经知道 Ruby 如何定义方法以及您如何调用方法。类似地，Ruby 有一个块的概念。
#
# 块由大量的代码组成。
# 您需要给块取个名称。
# 块中的代码总是包含在大括号 {} 内。
# 块总是从与其具有相同名称的函数调用。这意味着如果您的块名称为 test，那么您要使用函数 test 来调用这个块。
# 您可以使用 yield 语句来调用块。
# 语法
# block_name{
#    statement1
#    statement2
#    ..........
# }

def test
  puts "在 test 方法内"
  yield
  puts "你又回到了 test 方法内"
  yield
end
test {puts "你在块内"}
# 在 test 方法内
# 你在块内
# 你又回到了 test 方法内
# 你在块内
#

def test2
  yield 5
  puts "在 test 方法内"
  yield 100
end
test2 {|i| puts "你在块 #{i} 内"}
# 你在块 5 内
# 在 test 方法内
# 你在块 100 内

# TODO BEGIN 和 END 块
# 每个 Ruby 源文件可以声明当文件被加载时要运行的代码块（BEGIN 块），以及程序完成执行后要运行的代码块（END 块）
BEGIN {
  # BEGIN 代码块
  puts "BEGIN 代码块"
}

END {
  # END 代码块
  puts "END 代码块"
}
# MAIN 代码块
puts "MAIN 代码块"
