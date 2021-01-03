package main

//Go 语言的基础组成有以下几个部分：
//包声明
//引入包
//函数
//变量
//语句 & 表达式
//注释

import (
	"fmt"
)

func main() {
	var hello = "hello";
	world := "world";
	fmt.Println(hello + world);

	//TODO bool类型
	var b bool=true
	fmt.Println(b)
	var c=false
	fmt.Println(c)
	/**
	序号	类型和描述
	1	uint8
	无符号 8 位整型 (0 到 255)
	2	uint16
	无符号 16 位整型 (0 到 65535)
	3	uint32
	无符号 32 位整型 (0 到 4294967295)
	4	uint64
	无符号 64 位整型 (0 到 18446744073709551615)
	5	int8
	有符号 8 位整型 (-128 到 127)
	6	int16
	有符号 16 位整型 (-32768 到 32767)
	7	int32
	有符号 32 位整型 (-2147483648 到 2147483647)
	8	int64
	有符号 64 位整型 (-9223372036854775808 到 9223372036854775807)
	 */
	 var d int8=10
	fmt.Println(d)
	 e := 100
	fmt.Println(e)

	 //TODO 浮点型
	 /**
	1	float32
	IEEE-754 32位浮点型数
	2	float64
	IEEE-754 64位浮点型数
	3	complex64
	32 位实数和虚数
	4	complex128
	64 位实数和虚数
	  */

	//TODO 其他数据类型
	/**
	1	byte
	类似 uint8
	2	rune
	类似 int32
	3	uint
	32 或 64 位
	4	int
	与 uint 一样大小
	5	uintptr
	无符号整型，用于存放一个指针
		 */

}
