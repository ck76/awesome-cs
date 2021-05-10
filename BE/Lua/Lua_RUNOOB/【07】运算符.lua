
--其他运算符
--..	连接两个字符串	a..b ，其中 a 为 "Hello " ， b 为 "World", 输出结果为 "Hello World"。
--#	一元运算符，返回字符串或表的长度。	#"Hello" 返回 5
a = "Hello "
b = "World"

print("连接字符串 a 和 b ", a..b )
print("b 字符串长度 ",#b )
print("字符串 Test 长度 ",#"Test" )
print("菜鸟教程网址长度 ",#"www.runoob.com" )

tab1 = {"1","2"}
print("tab1长度"..#tab1)
--tab1长度2
tab2 = {key1="1","2"}
print("tab2长度"..#tab2)
--tab2长度1
tab3 = {}
tab3[1]="1"
tab3[2]="2"
tab3[4]="4"
print("tab3长度"..#tab3)
--tab3长度2
tab4 = {}
tab4[1] = "1"
tab4[2] = nil
tab4[3] = "2"
tab4[4] = nil
print("tab4的长度", #tab4)
--tab4的长度    1
tab5 = {}
tab5[1] = "1"
tab5[2] = nil
tab5[3] = "2"
tab5[4] = "4"
print("tab5的长度", #tab5)
--tab5的长度    4
tab6 = {1, nil, 3}
print("tab6的长度", #tab6)
--tab6的长度    3
tab6 = {1, nil, 3, nil}
print("tab6的长度", #tab6)
--tab6的长度    1
