

--Lua 语言中字符串可以使用以下三种方式来表示：
--
--单引号间的一串字符。
--双引号间的一串字符。
--[[ 与 ]] --间 的 一 串 字 符 。


string1 = "Lua"
print("\"字符串 1 是\"",string1)
string2 = 'runoob.com'
print("字符串 2 是",string2)

string3 = [["Lua 教程"]]
print("字符串 3 是",string3)

string1 = "Lua";
print(string.upper(string1))
print(string.lower(string1))

string = "Lua Tutorial"
-- 查找字符串
print(string.find(string,"Tutorial"))
reversedString = string.reverse(string)
print("新字符串为",reversedString)

--TODO 字符串格式化
--Lua 提供了 string.format() 函数来生成具有特定格式的字符串, 函数的第一个参数是格式 , 之后是对应格式中每个代号的各种数据。
--
--由于格式字符串的存在, 使得产生的长字符串可读性大大提高了。这个函数的格式很像 C 语言中的 printf()。
--
--以下实例演示了如何对字符串进行格式化操作：
--
--格式字符串可能包含以下的转义码:
--
--%c - 接受一个数字, 并将其转化为ASCII码表中对应的字符
--%d, %i - 接受一个数字并将其转化为有符号的整数格式
--%o - 接受一个数字并将其转化为八进制数格式
--%u - 接受一个数字并将其转化为无符号整数格式
--%x - 接受一个数字并将其转化为十六进制数格式, 使用小写字母
--%X - 接受一个数字并将其转化为十六进制数格式, 使用大写字母
--%e - 接受一个数字并将其转化为科学记数法格式, 使用小写字母e
--%E - 接受一个数字并将其转化为科学记数法格式, 使用大写字母E
--%f - 接受一个数字并将其转化为浮点数格式
--%g(%G) - 接受一个数字并将其转化为%e(%E, 对应%G)及%f中较短的一种格式
--%q - 接受一个字符串并将其转化为可安全被Lua编译器读入的格式
--%s - 接受一个字符串并按照给定的参数格式化该字符串
--为进一步细化格式, 可以在%号后添加参数. 参数将以如下的顺序读入:
--
--(1) 符号: 一个+号表示其后的数字转义符将让正数显示正号. 默认情况下只有负数显示符号.
--(2) 占位符: 一个0, 在后面指定了字串宽度时占位用. 不填时的默认占位符是空格.
--(3) 对齐标识: 在指定了字串宽度时, 默认为右对齐, 增加-号可以改为左对齐.
--(4) 宽度数值
--(5) 小数位数/字串裁切: 在宽度数值后增加的小数部分n, 若后接f(浮点数转义符, 如%6.3f)则设定该浮点数的小数只保留n位, 若后接s(字符串转义符, 如%5.3s)则设定该字符串只显示前n位.

string1 = "Lua"
string2 = "Tutorial"
number1 = 10
number2 = 20
-- 基本字符串格式化
print(string.format("基本格式化 %s %s",string1,string2))
-- 日期格式化
date = 2; month = 1; year = 2014
print(string.format("日期格式化 %02d/%02d/%03d", date, month, year))
-- 十进制格式化
print(string.format("%.4f",1/3))


string.format("%c", 83)                 -- 输出S
string.format("%+d", 17.0)              -- 输出+17
string.format("%05d", 17)               -- 输出00017
string.format("%o", 17)                 -- 输出21
string.format("%u", 3.14)               -- 输出3
string.format("%x", 13)                 -- 输出d
string.format("%X", 13)                 -- 输出D
string.format("%e", 1000)               -- 输出1.000000e+03
string.format("%E", 1000)               -- 输出1.000000E+03
string.format("%6.3f", 13)              -- 输出13.000
string.format("%q", "One\nTwo")         -- 输出"One\
                                                --Two"
string.format("%s", "monkey")           -- 输出monkey
string.format("%10s", "monkey")         -- 输出    monkey
string.format("%5.3s", "monkey")        -- 输出  mon


-- 字符转换
-- 转换第一个字符
print(string.byte("Lua"))
-- 转换第三个字符
print(string.byte("Lua",3))
-- 转换末尾第一个字符
print(string.byte("Lua",-1))
-- 第二个字符
print(string.byte("Lua",2))
-- 转换末尾第二个字符
print(string.byte("Lua",-2))
-- 整数 ASCII 码转换为字符
print(string.char(97))

string1 = "www."
string2 = "runoob"
string3 = ".com"
-- 使用 .. 进行字符串连接
print("连接字符串",string1..string2..string3)

-- 字符串长度
print("字符串长度 ",string.len(string2))

-- 字符串复制 2 次
repeatedString = string.rep(string2,2)
print(repeatedString)
