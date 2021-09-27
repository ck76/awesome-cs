package main

//Go 语言通过内置的错误接口提供了非常简单的错误处理机制。
//
//error类型是一个接口类型，这是它的定义：
//
//type error interface {
//    Error() string
//}

import (
	"fmt"
)

// 自定义错误信息结构
type DIV_ERR struct {
	etype int // 错误类型
	v1    int // 记录下出错时的除数、被除数
	v2    int
}

// 实现接口方法 error.Error()
func (div_err DIV_ERR) Error() string {
	if 0 == div_err.etype {
		return "除零错误"
	} else {
		return "其他未知错误"
	}
}

// 除法
func div(a int, b int) (int, *DIV_ERR) {
	if b == 0 {
		// 返回错误信息
		return 0, &DIV_ERR{0, a, b}
	} else {
		// 返回正确的商
		return a / b, nil
	}
}

func error_one() {
	// 正确调用
	v, r := div(100, 2)
	if nil != r {
		fmt.Println("(1)fail:", r)
	} else {
		fmt.Println("(1)succeed:", v)
	}
	// 错误调用
	v, r = div(100, 0)
	if nil != r {
		fmt.Println("(2)fail:", r)
	} else {
		fmt.Println("(2)succeed:", v)
	}
}
func main() {
	error_one()
	fmt.Println("##########################################")
	error_two()
}

func error_two() {
	fmt.Println("外层开始")
	defer func() {
		fmt.Println("外层准备recover")
		if err := recover(); err != nil {
			fmt.Printf("%#v-%#v\n", "外层", err) // err已经在上一级的函数中捕获了，这里没有异常，只是例行先执行defer，然后执行后面的代码
		} else {
			fmt.Println("外层没做啥事")
		}
		fmt.Println("外层完成recover")
	}()
	fmt.Println("外层即将异常")
	f()
	fmt.Println("外层异常后")
	defer func() {
		fmt.Println("外层异常后defer")
	}()
}

func f() {
	fmt.Println("内层开始")
	defer func() {
		fmt.Println("内层recover前的defer")
	}()

	defer func() {
		fmt.Println("内层准备recover")
		if err := recover(); err != nil {
			fmt.Printf("%#v-%#v\n", "内层", err) // 这里err就是panic传入的内容
		}

		fmt.Println("内层完成recover")
	}()

	defer func() {
		fmt.Println("内层异常前recover后的defer")
	}()

	panic("异常信息")

	defer func() {
		fmt.Println("内层异常后的defer")
	}()

	fmt.Println("内层异常后语句") //recover捕获的一级或者完全不捕获这里开始下面代码不会再执行
}
