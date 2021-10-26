#https://iowiki.com/elixir/elixir_keyword_lists.html

#到目前为止，我们还没有讨论任何关联数据结构，即可以将特定值（或多个值）与密钥相关联的数据结构。 不同的语言使用不同的名称来调用这些功能，如字典，散列，关联数组等。
#
#在Elixir中，我们有两个主要的关联数据结构:关键字列表和映射。 在本章中，我们将重点关注关键字列表。
#
#在许多函数式编程语言中，通常使用2项元组的列表作为关联数据结构的表示。 在Elixir中，当我们有一个元组列表并且元组的第一项（即键）是一个原子时，我们将其称为关键字列表。 考虑以下示例来理解相同的 -

list_1 = [{:a, 1}, {:b, 2}]
list_2 = [a: 1, b: 2]
IO.puts(list_1 == list_2)
#true


list = [a: 1, b: 2]
IO.puts(list[:a])
#1

#关键字列表有三个特点 -
    #Keys must be atoms.
    #根据开发人员的指定订购密钥。
    #钥匙可以多次出现。
##为了操纵关键字列表，Elixir提供了关键字模块 。
#但请记住，关键字列表只是列表，因此它们提供与列表相同的线性性能特征。
#列表越长，查找密钥，计算项目数量等所需的时间越长，等等。
#因此，Elixir中的关键字列表主要用作选项。
#如果您需要存储许多项目或保证具有最大单值的一键关联，则应使用地图。
