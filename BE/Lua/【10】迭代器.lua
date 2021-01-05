
--迭代器（iterator）是一种对象，它能够用来遍历标准模板库容器中的部分或全部元素，每个迭代器对象代表容器中的确定的地址。
--在 Lua 中迭代器是一种支持指针类型的结构，它可以遍历集合的每一个元素。
--泛型 for 在自己内部保存迭代函数，实际上它保存三个值：迭代函数、状态常量、控制变量。
--
--泛型 for 迭代器提供了集合的 key/value 对，语法格式如下：
--for k, v in pairs(t) do
--    print(k, v)
--end


array = {"Google", "Runoob"}

for key,value in ipairs(array)
do
    print(key, value)
end
--下面我们看看泛型 for 的执行过程：
--
--首先，初始化，计算 in 后面表达式的值，表达式应该返回泛型 for 需要的三个值：迭代函数、状态常量、控制变量；
-- 与多值赋值一样，如果表达式返回的结果个数不足三个会自动用 nil 补足，多出部分会被忽略。
--第二，将状态常量和控制变量作为参数调用迭代函数（注意：对于 for 结构来说，状态常量没有用处，仅仅在初始化时获取他的值并传递给迭代函数）。
--第三，将迭代函数返回的值赋给变量列表。
--第四，如果返回的第一个值为nil循环结束，否则执行循环体。
--第五，回到第二步再次调用迭代函数
--在Lua中我们常常使用函数来描述迭代器，每次调用该函数就返回集合的下一个元素。Lua 的迭代器包含以下两种类型：
--
--无状态的迭代器
--多状态的迭代器

--TODO 无状态的迭代器
function square(iteratorMaxCount,currentNumber)
    if currentNumber<iteratorMaxCount
    then
        currentNumber = currentNumber+1
        return currentNumber, currentNumber*currentNumber
    end
end

for i,n in square,3,0
do
    print(i,n)
end



function iter (a, i)
    i = i + 1
    local v = a[i]
    if v then
        return i, v
    end
end

function ipairs (a)
    return iter, a, 0
end
--当 Lua 调用 ipairs(a) 开始循环时，他获取三个值：迭代函数 iter、状态常量 a、控制变量初始值 0；
-- 然后 Lua 调用 iter(a,0) 返回 1, a[1]（除非 a[1]=nil）；第二次迭代调用 iter(a,1) 返回 2, a[2]……直到第一个 nil 元素。

--TODO 多状态的迭代器
--很多情况下，迭代器需要保存多个状态信息而不是简单的状态常量和控制变量，最简单的方法是使用闭包，
-- 还有一种方法就是将所有的状态信息封装到 table 内，将 table 作为迭代器的状态常量，因为这种情况下可以将所有的信息存放在 table 内，所以迭代函数通常不需要第二个参数。
--以下实例我们创建了自己的迭代器：
array = {"Google", "Runoob"}

function elementIterator (collection)
    local index = 0
    local count = #collection
    -- 闭包函数
    return function ()
        index = index + 1
        if index <= count
        then
            --  返回迭代器的当前元素
            return collection[index]
        end
    end
end

for element in elementIterator(array)
do
    print(element)
end


--TODO pairs 和 ipairs区别
-- pairs: 迭代 table，可以遍历表中所有的 key 可以返回 nil
-- ipairs: 迭代数组，不能返回 nil,如果遇到 nil 则退出
local tab= {
    [1] = "a",
    [3] = "b",
    [4] = "c"
}
for i,v in pairs(tab) do        -- 输出 "a" ,"b", "c"  ,
    print( tab[i] )
end

for i,v in ipairs(tab) do    -- 输出 "a" ,k=2时断开
    print( tab[i] )
end
