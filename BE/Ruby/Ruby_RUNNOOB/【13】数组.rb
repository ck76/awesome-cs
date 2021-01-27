# TODO Ruby 数组（Array）
# Ruby 数组是任何对象的有序整数索引集合。数组中的每个元素都与一个索引相关，并可通过索引进行获取。
#
# 数组的索引从 0 开始，这与 C 或 Java 中一样。一个负数的索相对于数组的末尾计数的，也就是说，索引为 -1 表示数组的最后一个元素，-2 表示数组中的倒数第二个元素，依此类推。
#
# Ruby 数组可存储诸如 String、 Integer、 Fixnum、 Hash、 Symbol 等对象，甚至可以是其他 Array 对象。
#
# Ruby 数组不需要指定大小，当向数组添加元素时，Ruby 数组会自动增长。
#
#
#!/usr/bin/ruby

names = Array.new(20)
puts names.size # 返回 20
puts names.length # 返回 20


names = Array.new(4, "mac")
puts "#{names}"

nums = Array.new(10) {|e| e = e * 2}
puts "#{nums}"

nums = Array.[](1, 2, 3, 4, 5)

nums = Array[1, 2, 3, 4, 5]

digits = Array(0..9)

puts "#{digits}"

# Array.[](...) [or] Array[...] [or] [...]

a = ["a", "b", "c"]
n = [65, 66, 67]
puts a.pack("A3A3A3") #=> "a  b  c  "
puts a.pack("a3a3a3") #=> "a\000\000b\000\000c\000\000"
puts n.pack("ccc") #=> "ABC"
