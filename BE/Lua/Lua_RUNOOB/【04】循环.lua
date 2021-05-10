
--TODO cintinue
--lua 中没有 continue 语句有点不习惯。
--可以使用类似下面这种方法实现 continue 语句：
for i = 10, 1, -1 do
    repeat
        if i == 5 then
            print("continue code here")
            break
        end
        print(i, "loop code here")
    until true
end


--TODO while循环
a = 10
while (a<20)
    do
    print( "a的值是",a)
    a=a+1
end

--TODO for Lua 编程语言中数值 for 循环语法格式:
--for var=exp1,exp2,exp3 do
--    <执行体>
--end
--var 从 exp1 变化到 exp2，每次变化以 exp3 为步长递增 var，并执行一次 "执行体"。exp3 是可选的，如果不指定，默认为1。
function f(x)
    print("function")
    return x*2
end

for i=1,f(5)
    do print(i)
end


--打印数组a的所有值
--泛型for循环
--泛型 for 循环通过一个迭代器函数来遍历所有值，类似 java 中的 foreach 语句。
--Lua 编程语言中泛型 for 循环语法格式
a = {"one", "two", "three"}
for i, v in ipairs(a) do
    print(i, v)
end


--TODO Lua repeat...until 循环
--Lua 编程语言中 repeat...until 循环语句不同于 for 和 while循环，for 和 while 循环的条件语句在当前循环执行开始时判断，而 repeat...until 循环的条件语句在当前循环结束后判断。
--[ 变量定义 --]
a = 10
--[ 执行循环 --]
repeat
    print("a的值为:", a)
    a = a + 1
until( a > 15 )

--TODO 嵌套循环
j=2
for i=2,10 do
    for j=2,(i/j) do
        if (not (i%j)) then
            break
        end
        if (j>(i/j)) then
            print("i 的值为：",i)
        end
    end
end

