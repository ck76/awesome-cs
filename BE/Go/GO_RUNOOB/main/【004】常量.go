package main

import (
	"fmt"
	"unsafe"
)

//常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。
//常量的定义格式：
//const identifier [type] = value

const (
	Unknown = 0
	Female  = 1
	Male    = 2
)

const (
	a1 = "abc"
	b1 = len(a1)
	c1 = unsafe.Sizeof(a1)
)

const (
	ck = iota
	ck1
	ck2
)

const (
	a = iota //0
	b        //1
	c        //2
	d = "ha" //独立值，iota += 1  		ha
	e        //"ha"   iota += 1 		ha
	f = 100  //iota +=1				100
	g        //100  iota +=1			100
	h = iota //7,恢复计数				7
	i        //8						8
)

//TODO iota 只是在同一个 const 常量组内递增，每当有新的 const 关键字时，iota 计数会重新开始。
const xx = iota
const yy = iota
const (
	i1 = iota
	j  = iota
	x  = iota
)

func main() {
	const_var()
	println(a1, b1, c1)                    //abc 3 16
	fmt.Println(a, b, c, d, e, f, g, h, i) //0 1 2 ha ha 100 100 7 8
	println(i1, j, x, xx, yy)              //0 1 2 0 0

}

func const_var() {
	const LENGTH int = 10
	const WIDTH int = 5
	var area int
	//const a, b, c = 1, false, "str" //多重赋值

	area = LENGTH * WIDTH
	fmt.Println("面积为 : %d", area)
	println()
	//println(a, b, c)
}
