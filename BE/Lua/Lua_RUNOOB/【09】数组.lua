

--TODO 一维
array = {"Lua", "Tutorial"}
for i= 0, 2 do
    print(array[i])
end


array = {}
for i= -2, 2 do
    array[i] = i *2
end
for i = -2,2 do
    print(array[i])
end

--多维数组
-- 初始化数组
array = {}
for i=1,3 do
    array[i] = {}
    for j=1,3 do
        array[i][j] = i*j
    end
end

-- 访问数组
for i=1,3 do
    for j=1,3 do
        print(array[i][j])
    end
end
