#https://iowiki.com/elixir/elixir_decision_making.html

#❎ if 语句
a = true
if a === true do
  IO.puts "Variable a is true!"
  IO.puts "So this code block is executed"
end
IO.puts "Outside the if statement"

#❎ if..else statement
a = false
if a === true do
  IO.puts "Variable a is true!"
else
  IO.puts "Variable a is false!"
end
IO.puts "Outside the if statement"


#❎ unless statement
#如果布尔表达式的计算结果为false ，则将执行unless语句中的代码块。
#如果布尔表达式的计算结果为true，则将执行给定除非语句的结束关键字之后的第一组代码。
a = false
unless a === true do
  IO.puts "Condition is not satisfied"
  IO.puts "So this code block is executed"
end
IO.puts "Outside the unless statement"

#结果如下
#Condition is not satisfied
#So this code block is executed
#Outside the unless statement

#❎ unless..else statement
a = false
unless a === false do
  IO.puts "Condition is not satisfied"
else
  IO.puts "Condition was satisfied!"
end
IO.puts "Outside the unless statement"
#Condition was satisfied!
#Outside the unless statement

#❎ cond
#在我们想要在几个条件的基础上执行代码的地方使用Cond语句。
#它的工作方式类似于其他几种编程语言中的if ... .else结构。
guess = 46
cond do
  guess == 10 -> IO.puts "You guessed 10!"
  guess == 46 -> IO.puts "You guessed 46!"
  guess == 42 -> IO.puts "You guessed 42!"
  true        -> IO.puts "I give up."
end

#❎ case
#Case语句可以被视为命令式语言中switch语句的替代。
case 3 do
  1 -> IO.puts("Hi, I'm one")
  2 -> IO.puts("Hi, I'm two")
  3 -> IO.puts("Hi, I'm three")
  _ -> IO.puts("Oops, you dont match!")
end