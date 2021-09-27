package main
import "fmt"
//Go 语言中变量可以在三个地方声明：
//
//函数内定义的变量称为局部变量
//函数外定义的变量称为全局变量
//函数定义中的变量称为形式参数

func main() {
	local()
	global()
}

func local(){
	/* 声明局部变量 */
	var a, b, c int

	/* 初始化参数 */
	a = 10
	b = 20
	c = a + b

	fmt.Printf ("结果： a = %d, b = %d and c = %d\n", a, b, c)
}

/* 声明全局变量 */
var g int

func global(){
	//TODO Go 语言程序中全局变量与局部变量名称可以相同，但是函数内的局部变量会被优先考虑
	/* 声明局部变量 */
	var a, b int

	/* 初始化参数 */
	a = 10
	b = 20
	g = a + b

	fmt.Printf("结果： a = %d, b = %d and g = %d\n", a, b, g)
}
