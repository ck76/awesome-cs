# TODO Ruby 异常
# 异常和执行总是被联系在一起。如果您打开一个不存在的文件，且没有恰当地处理这种情况，那么您的程序则被认为是低质量的。
#
# 如果异常发生，则程序停止。异常用于处理各种类型的错误，这些错误可能在程序执行期间发生，所以要采取适当的行动，而不至于让程序完全停止。
#
# Ruby 提供了一个完美的处理异常的机制。我们可以在 begin/end 块中附上可能抛出异常的代码，并使用 rescue 子句告诉 Ruby 完美要处理的异常类型。
#
## -------------------------------------
#
# 语法
# begin #开始
#
#  raise.. #抛出异常
#
# rescue [ExceptionType = StandardException] #捕获指定类型的异常默认值是 StandardException
#  $! #表示异常信息
#  $@ #表示异常出现的代码位置
# else #其余异常
#  ..
# ensure #不管有没有异常，进入该代码块
#
# end #结束
#
# -------------------------------------
#
# 从 begin 到 rescue 中的一切是受保护的。如果代码块执行期间发生了异常，控制会传到 rescue 和 end 之间的块。
#
# 对于 begin 块中的每个 rescue 子句，Ruby 把抛出的异常与每个参数进行轮流比较。如果 rescue 子句中命名的异常与当前抛出的异常类型相同，或者是该异常的父类，则匹配成功。
#
# 如果异常不匹配所有指定的错误类型，我们可以在所有的 rescue 子句后使用一个 else 子句。
#
begin
  file = open("/unexistant_file")
  if file
    puts "File opened successfully"
  end
rescue
  file = STDIN
end
print file, "=================", STDIN, "\n"

# 以上实例运行输出结果为。您可以看到，STDIN 取代了 file ，因为打开失败。
#
# #<IO:0xb7d16f84>==#<IO:0xb7d16f84>

# TODO 使用 retry 语句
$fname = "/unexistant_file"
begin
  file = open($fname)
  if file
    puts "File opened successfully"
  end
rescue
  $fname = "existant_file"
  retry
#   注意：如果被重新命名的文件不存在，本实例代码会无限尝试。所以异常处理时，谨慎使用 retry。
end


# TODO 使用 raise 语句
# 您可以使用 raise 语句抛出异常。下面的方法在调用时抛出异常。它的第二个消息将被输出。
begin
  puts 'I am before the raise.'
  raise 'An error has occurred.'
  puts 'I am after the raise.'
rescue
  puts 'I am rescued.'
end
puts 'I am after the begin block.'

begin
  raise 'A test exception.'
rescue Exception => e
  puts e.message
  puts e.backtrace.inspect
end

# TODO 使用 ensure 语句
# 有时候，无论是否抛出异常，您需要保证一些处理在代码块结束时完成。例如，您可能在进入时打开了一个文件，当您退出块时，您需要确保关闭文件。
#
# ensure 子句做的就是这个。ensure 放在最后一个 rescue 子句后，并包含一个块终止时总是执行的代码块。它与块是否正常退出、是否抛出并处理异常、是否因一个未捕获的异常而终止，这些都没关系，
# ensure 块始终都会运行。
#语法
begin
  #.. 过程
  #.. 抛出异常
rescue
  #.. 处理错误
ensure
  #.. 最后确保执行
  #.. 这总是会执行
end


begin
  raise 'A test exception.'
rescue Exception => e
  puts e.message
  puts e.backtrace.inspect
ensure
  puts "Ensuring execution"
end

# TODO 使用 else 语句
# 如果提供了 else 子句，它一般是放置在 rescue 子句之后，任意 ensure 之前。
#
# else 子句的主体只有在代码主体【没有】抛出异常时执行。
#
begin
  #.. 过程
  #.. 抛出异常
rescue
  #.. 处理错误
else
  #.. 如果没有异常则执行
ensure
  #.. 最后确保执行
  #.. 这总是会执行
end

begin
  # 抛出 'A test exception.'
  puts "I'm not raising exception"
rescue Exception => e
  puts e.message
  puts e.backtrace.inspect
else
  puts "Congratulations-- no errors!"
ensure
  puts "Ensuring execution"
end


# TODO Catch 和 Throw
# raise 和 rescue 的异常机制能在发生错误时放弃执行，有时候需要在正常处理时跳出一些深层嵌套的结构。此时 catch 和 throw 就派上用场了。
#
# catch 定义了一个使用给定的名称（可以是 Symbol 或 String）作为标签的块。块会正常执行直到遇到一个 throw。
throw :lablename
#.. 这不会被执行
catch :lablename do
#.. 在遇到一个 throw 后匹配将被执行的 catch
end

或

throw :lablename #condition
#.. 这不会被执行
catch :lablename do
#.. 在遇到一个 throw 后匹配将被执行的 catch
end


def promptAndGet(prompt)
  print prompt
  res = readline.chomp
  throw :quitRequested if res == "!"
  return res
end

catch :quitRequested do
  name = promptAndGet("Name: ")
  age = promptAndGet("Age: ")
  sex = promptAndGet("Sex: ")
  # ..
  # 处理信息
end
promptAndGet("Name:")
# Name: Ruby on Rails
# Age: 3
# Sex: !
# Name:Just Ruby
#

# TODO 类 Exception
# Ruby 的标准类和模块抛出异常。所有的异常类组成一个层次，包括顶部的 Exception 类在内。下一层是七种不同的类型：
#
# Interrupt
# NoMemoryError
# SignalException
# ScriptError
# StandardError
# SystemExit
# Fatal 是该层中另一种异常，但是 Ruby 解释器只在内部使用它。
#
# ScriptError 和 StandardError 都有一些子类，但是在这里我们不需要了解这些细节。最重要的事情是创建我们自己的异常类，它们必须是类 Exception 或其子代的子类。
class FileSaveError < StandardError
  attr_reader :reason

  def initialize(reason)
    @reason = reason
  end
end
File.open(path, "w") do |file|
  begin
    # 写出数据 ...
  rescue
    # 发生错误
    raise FileSaveError.new($!)
  end
end
# 在这里，最重要的一行是 raise FileSaveError.new($!)。我们调用 raise 来示意异常已经发生，把它传给 FileSaveError 的一个新的实例，由于特定的异常引起数据写入失败。
