#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

phone = "138-3453-1111 #这是一个电话号码"

# 删除 Ruby 的注释
phone = phone.sub!(/#.*$/, "")
puts "电话号码 : #{phone}"

# 移除数字以外的其他字符
phone = phone.gsub!(/\D/, "")
puts "电话号码 : #{phone}"
