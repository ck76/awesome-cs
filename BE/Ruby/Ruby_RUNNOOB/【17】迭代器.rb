# TODO 简单来说：迭代(iterate)指的是重复做相同的事，所以迭代器(iterator)就是用来重复多次相同的事。
#
# 迭代器是集合支持的方法。存储一组数据成员的对象称为集合。在 Ruby 中，数组(Array)和哈希(Hash)可以称之为集合。
#
# 迭代器返回集合的所有元素，一个接着一个。在这里我们将讨论两种迭代器，each 和 collect。
#
#
#
# TODO Ruby each 迭代器
ary = [1, 2, 3, 4, 5]
ary.each do |i|
  puts i
end
# 以上实例运行输出结果为：
#
# 1
# 2
# 3
# 4
# 5
# each 迭代器总是与一个块关联。它向块返回数组的每个值，一个接着一个。值被存储在变量 i 中，然后显示在屏幕上。
#


# TODO Ruby collect 迭代器
# collect 迭代器返回集合的所有元素。
# collect 方法不需要总是与一个块关联。collect 方法返回整个集合，不管它是数组或者是哈希。
a = [1, 2, 3, 4, 5]
b = Array.new
b = a.collect {|x| x + 1}
puts b


# Java需要把Map转化成List类型的容器才能使用迭代器，但Ruby有直接针对Map的迭代器：

sum = 0
cutcome = {:block1 => 1000, :book2 => 1000, :book3 => 4000}
cutcome.each {|item, price| sum += price}
print "sum = " + sum.to_s
# 甚至还可以这样：

sum = 0
cutcome = {"block1" => 1000, "book2" => 1000, "book3" => 4000}
cutcome.each {|pair| sum += pair[1]}
print "sum = " + sum.to_s
