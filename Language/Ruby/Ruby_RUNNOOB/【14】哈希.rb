#!/usr/bin/ruby

months = Hash.new( "month" )

puts "#{months[0]}"
# 当您访问带有默认值的哈希中的任意键时，如果键或值不存在，访问哈希将返回默认值：
puts "#{months[72]}"
# month
# month
#

H = Hash[:a => 100, "b" => 200]
puts "#{H['a']}"
puts "#{H['b']}"


$, = ", "
months = Hash.new( "month" )
months = {"1" => "January", "2" => "February"}
keys = months.keys
puts "#{keys}"
# ["1", "2"]
