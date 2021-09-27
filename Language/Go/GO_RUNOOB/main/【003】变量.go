package main

import "fmt"

var x, y int
var (
	// 这种因式分解关键字的写法一般用于声明全局变量
	//全局变量是允许声明但不使用的
	a int  = 1000
	b bool = true
)
var c, d int = 1, 2
var e, f = 123, "hello"

//这种不带声明格式的只能在函数体中出现
//g, h := 123, "hello"

func main() {
	define()
	global_var()
	short_define()
	numbers()
}

/**
一个可以返回多个值的函数
 */
func numbers()(int,int,string){
	a , b , c := 1 , 2 , "str"
	return a,b,c
}

/**
全局变量
 */
func global_var() {
	g, h := 123, "hello"
	println(x, y, a, b, c, d, e, f, g, h)
	//	0 0 1000 true 1 2 123 hello 123 hello
}

/**
简短声明
 */
func short_define() {
	//简短声明类型推断
	a := "abc"
	fmt.Println(a)
	g, h := 100, "s"
	fmt.Println(g,h)
}

/**
变量定义
 */
func define() {
	var a string = "Runoob"
	fmt.Println(a)

	var b, c int = 1, 2
	fmt.Println(b, c)

	//--------------------------------
	// 声明一个变量并初始化
	var d = "RUNOOB"
	fmt.Println(d)

	// 没有初始化就为零值
	var e int
	fmt.Println(e)

	// bool 零值为 false
	var f bool
	fmt.Println(f)
	/**
	数值类型（包括complex64/128）为 0

	布尔类型为 false

	字符串为 ""（空字符串）

	以下几种类型为 nil：

	var a *int
	var a []int
	var a map[string] int
	var a chan int
	var a func(string) int
	var a error // error 是接口
	 */
}
