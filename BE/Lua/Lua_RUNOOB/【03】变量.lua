

--Lua 变量有三种类型：全局变量、局部变量、表中的域。
--Lua 中的变量全是全局变量，那怕是语句块或是函数里，除非用 local 显式声明为局部变量。
--局部变量的作用域为从声明位置开始到所在语句块结束。
--变量的默认值均为 nil

a = 5               -- 全局变量
local b = 5         -- 局部变量

function joke()
    c = 5           -- 全局变量
    local d = 6     -- 局部变量
end

joke()
print(c,d)          --> 5 nil

do
    local a = 6     -- 局部变量
    b = 6           -- 对局部变量重新赋值
    print(a,b);     --> 6 6
end

print(a,b)      --> 5 6


--TODO 赋值语句-------------------------
a, b, c = 0, 1
print(a,b,c)             --> 0   1   nil

a, b = a+1, b+1, b+2     -- value of b+2 is ignored
print(a,b)               --> 1   2

a, b, c = 0
print(a,b,c)             --> 0   nil   nil

a, b, c = 0, 0, 0
print(a,b,c)             --> 0   0   0



--TODO 索引
site = {}
site["key"]="www.ck.com"
print(site["key"])
print(site.key) --效果相同
