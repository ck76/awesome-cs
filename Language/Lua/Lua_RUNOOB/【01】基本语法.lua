
--

--[[
 多行注释
 多行注释
 --]]

--[[
print('多行注释')

--]]
---[[
print('取消多行注释')
--]]


-- TODO 关键词
--以下列出了 Lua 的保留关键词。保留关键字不能作为常量或变量或其他用户自定义标示符：
--
--and	break	do	else
--elseif	end	false	for
--function	if	in	local
--nil	not	or	repeat
--return	then	true	until
--while	goto
--一般约定，以下划线开头连接一串大写字母的名字（比如 _VERSION）被保留用于 Lua 内部全局变量。

--TODO 全局变量
--在默认情况下，变量总是认为是全局的。
--
--全局变量不需要声明，给一个变量赋值后即创建了这个全局变量，访问一个没有初始化的全局变量也不会出错，只不过得到的结果是：nil。

print(b)--nil
b=10
print(b)
