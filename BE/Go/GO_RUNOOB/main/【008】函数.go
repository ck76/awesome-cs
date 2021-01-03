package main

import (
	"fmt"
	"math"
)

func main() {
	/* 定义局部变量 */
	var a int = 100
	var b int = 200
	var ret int

	/* TODO 调用函数并返回最大值 */
	ret = max(a, b)

	fmt.Printf("最大值是 : %d\n", ret)

	//	TODO 多返回值----------------------
	c, d := swap("Google", "Runoob")
	fmt.Println(c, d)

	//	TODO 引用传递-------------------------------------------
	/* 调用 swap() 函数
	* &a 指向 a 指针，a 变量的地址
	* &b 指向 b 指针，b 变量的地址
	*/
	swap_ref(&a, &b)

	fmt.Printf("交换后，a 的值 : %d\n", a)
	fmt.Printf("交换后，b 的值 : %d\n", b)

	//	TODO 函数作为实参
	func_arg()
	// TODO 闭包
clousure()
	// TODO 方法

}

/* 函数返回两个数的最大值 */
func max(num1, num2 int) int {
	/* 定义局部变量 */
	var result int

	if (num1 > num2) {
		result = num1
	} else {
		result = num2
	}
	return result
}

/**
多返回值
 */
func swap(x, y string) (string, string) {
	return y, x
}

//函数参数
//函数如果使用参数，该变量可称为函数的形参。
//
//形参就像定义在函数体内的局部变量。
//
//调用函数，可以通过两种方式来传递参数：
//
//传递类型	描述
//值传递	值传递是指在调用函数时将实际参数复制一份传递到函数中，这样在函数中如果对参数进行修改，将不会影响到实际参数。
//引用传递	引用传递是指在调用函数时将实际参数的地址传递到函数中，那么在函数中对参数所进行的修改，将影响到实际参数。
//【默认情况下】，Go 语言使用的是值传递，即在调用过程中不会影响到实际参数。
/**
引用传递
 */
func swap_ref(x *int, y *int) {
	var temp int
	temp = *x /* 保持 x 地址上的值 */
	*x = *y   /* 将 y 值赋给 x */
	*y = temp /* 将 temp 值赋给 y */
}

/**
函数作为参数
 */

func func_arg() {
	/* 声明函数变量 */
	getSquareRoot := func(x float64) float64 {
		return math.Sqrt(x)
	}

	/* 使用函数 */
	fmt.Println(getSquareRoot(9))
	//	---------------
	testCallBack(1, callBack)
	testCallBack(2, func(x int) int {
		fmt.Printf("我是回调，x：%d\n", x)
		return x
	})
}

// 声明一个函数类型
type cb func(int) int

func testCallBack(x int, f cb) {
	f(x)
}

func callBack(x int) int {
	fmt.Printf("我是回调，x：%d\n", x)
	return x
}

/**
闭包
 */

func clousure() {
	/* nextNumber 为一个函数，函数 i 为 0 */
	nextNumber := getSequence()

	/* 调用 nextNumber 函数，i 变量自增 1 并返回 */
	fmt.Println(nextNumber())
	fmt.Println(nextNumber())
	fmt.Println(nextNumber())

	/* 创建新的函数 nextNumber1，并查看结果 */
	nextNumber1 := getSequence()
	fmt.Println(nextNumber1())
	fmt.Println(nextNumber1())
//	add fun
	add_func := add(1, 2)
	fmt.Println(add_func(4, 5))
	fmt.Println(add_func(1, 3))
	fmt.Println(add_func(2, 2))
}
func getSequence() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}

// 闭包使用方法
//// 闭包使用方法，函数声明中的返回值(闭包函数)不用写具体的形参名称
//func add(x1, x2 int) func(int, int) (int, int, int) {
func add(x1, x2 int) func(x3 int,x4 int)(int,int,int)  {
	i := 0
	return func(x3 int,x4 int) (int,int,int){
		i++
		return i,x1+x2,x3+x4
	}
}

/**
方法
 */
// Go 语言中同时有函数和方法。一个方法就是一个包含了接受者的函数，接受者可以是命名类型或者结构体类型的一个值或者是一个指针。
// 所有给定类型的方法属于该类型的方法集。语法格式如下：
//
//func (variable_name variable_data_type) function_name() [return_type]{
//   /* 函数体*/
//}

/* 定义结构体 */
type Circle struct {
	radius float64
}

func method(){
	var c1 Circle
	c1.radius = 10.00
	fmt.Println("圆的面积 = ", c1.getArea())
}
//该 method 属于 Circle 类型对象中的方法
func (c Circle) getArea() float64 {
	//c.radius 即为 Circle 类型对象中的属性
	return 3.14 * c.radius * c.radius
}

//在 C++ 中是这样的:
//
//class Circle {
//  public:
//    float getArea() {
//       return 3.14 * radius * radius;
//    }
//  private:
//    float radius;
//}
//
//// 其中 getArea 经过编译器处理大致变为
//float getArea(Circle *const c) {
//  ...
//}
