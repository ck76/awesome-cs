#!/usr/bin/ruby -w

require "dbi"

begin
  # 连接到 MySQL 服务器
  dbh = DBI.connect("DBI:Mysql:TESTDB:localhost",
                    "root", "")
  # 获取服务器版本字符串，并显示
  row = dbh.select_one("SELECT VERSION()")
  puts "Server version: " + row[0]
rescue DBI::DatabaseError => e
  puts "An error occurred"
  puts "Error code:    #{e.err}"
  puts "Error message: #{e.errstr}"
ensure
  # 断开与服务器的连接
  dbh.disconnect if dbh
end
