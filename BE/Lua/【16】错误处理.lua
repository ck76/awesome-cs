function add(a, b)
    return a + b
end

local function add(a,b)
    assert(type(a) == "number", "a 不是一个数字")
    assert(type(b) == "number", "b 不是一个数字")
    return a+b
end

print(add(10, 20))
add(10)
