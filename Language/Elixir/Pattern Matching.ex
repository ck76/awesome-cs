#https://iowiki.com/elixir/elixir_pattern_matching.html

x = 12
x = "ck"
IO.puts x


#== Compilation error in file Pattern Matching.ex ==
#** (Protocol.UndefinedError) protocol String.Chars not implemented for {"First variable"} of type Tuple
#    (elixir 1.12.2) lib/string/chars.ex:3: String.Chars.impl_for!/1
#    (elixir 1.12.2) lib/string/chars.ex:22: String.Chars.to_string/1
#    (elixir 1.12.2) lib/io.ex:712: IO.puts/2
#    Pattern Matching.ex:7: (file)
#todo 如果用{"First variable}就会报↑的错误❌
[var_1, _unused_var, var_2] = [["First variable"], 25, "Second variable" ]
IO.puts(var_1)
IO.puts(var_2)

#这将在var_1存储值{"First variable"} ，在var_2中var_2 "Second variable" 。
#还有一个特殊的_变量（或以'_'为前缀的变量），其工作方式与其他变量完全相同，但告诉elixir，
#"Make sure something is here, but I don't care exactly what it is." 。
#在前面的例子中， _unused_var就是这样一个变量。

[_, [_, {a}]] = ["Random string", [:an_atom, {24}]]
IO.puts(a)

#在模式匹配中，如果我们在right使用变量，则使用其值。 如果要使用左侧变量的值，则需要使用pin运算符。
#例如，如果您的变量“a”的值为25，并且您希望将其与另一个值为25的变量“b”匹配，那么您需要输入 -
a = 25
b = 25
^a=b
IO.puts(^a=b)  #25

#❌== Compilation error in file Pattern Matching.ex ==
#** (MatchError) no match of right hand side value: 26
#    Pattern Matching.ex:29: (file)
#    (elixir 1.12.2) lib/kernel/parallel_compiler.ex:319: anonymous fn/4 in Kernel.ParallelCompiler.spawn_workers/7