
--[ 0 为 true ]
if(0)
then
    print("0 为 true")
end


--[ 定义变量 --]
a = 100;
b = 200;

--[ 检查条件 --]

if( a < 20 )
then
    --[ if 条件为 true 时执行该语句块 --]
    print("a 小于 20" )
else
    --[ if 条件为 false 时执行该语句块 --]
    print("a 大于 20" )
end


if( a == 100 )
then
    --[ if 条件为 true 时执行以下 if 条件判断 --]
    if( b == 200 )
    then
        --[ if 条件为 true 时执行该语句块 --]
        print("a 的值为 100 b 的值为 200" );
    end
end
print("a 的值为 :", a );
print("b 的值为 :", b );
