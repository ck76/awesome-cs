#!/usr/bin/ruby
# -*- coding: UTF-8 -*-
# TODO while
#
$i = 0
$num = 5

while $i < $num do
  puts("在循环语句中 i = #$i")
  $i += 1
end

$i = 0
$num = 5
begin
  puts("在循环语句中 i = #$i")
  $i += 1
end while $i < $num


# TODO until
$i = 0
$num = 5

until $i > $num do
  puts("在循环语句中 i = #$i")
  $i += 1;
end

# TODO Ruby until 修饰符
$i = 0
$num = 5
begin
  puts("在循环语句中 i = #$i")
  $i += 1;
end until $i > $num

# TODO Ruby for 语句
for i in 0..5
  puts "局部变量的值为 #{i}"
end

(0..5).each do |i|
  puts "局部变量的值为 #{i}"
end


# TODO Ruby break 语句
for i in 0..5
  if i > 2 then
    break
  end
  puts "局部变量的值为 #{i}"
end

# TODO Ruby next 语句
for i in 0..5
  if i < 3 then
    next
  end
  puts "局部变量的值为 #{i}"
end

# TODO Ruby redo 语句
for i in 0..5
  if i < 2 then
    puts "局部变量的值为 #{i}"
    redo
  end
end

# TODO Ruby retry 语句
for i in 1..5
  retry if i > 2
  puts "局部变量的值为 #{i}"
end
