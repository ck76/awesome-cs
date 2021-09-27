package main

import "fmt"

//if 语句	if 语句 由一个布尔表达式后紧跟一个或多个语句组成。
//if...else 语句	if 语句 后可以使用可选的 else 语句, else 语句中的表达式在布尔表达式为 false 时执行。
//if 嵌套语句	你可以在 if 或 else if 语句中嵌入一个或多个 if 或 else if 语句。
//switch 语句	switch 语句用于基于不同条件执行不同动作。
//select 语句	select 语句类似于 switch 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。

func main() {
	select_()
}

//以下描述了 select 语句的语法：
//
//每个 case 都必须是一个通信
//所有 channel_no_buffer 表达式都会被求值
//所有被发送的表达式都会被求值
//如果任意某个通信可以进行，它就执行，其他被忽略。
//如果有多个 case 都可以运行，Select 会随机公平地选出一个执行。其他不会执行。
//否则：
//如果有 default 子句，则执行该语句。
//如果没有 default 子句，select 将阻塞，直到某个通信可以运行；Go 不会重新对 channel_no_buffer 或值进行求值。
func select_() {
	var c1, c2, c3 chan int
	var i1, i2 int
	select {
	case i1 = <-c1:
		fmt.Printf("received ", i1, " from c1\n")
	case c2 <- i2:
		fmt.Printf("sent ", i2, " to c2\n")
	case i3, ok := (<-c3): // same as: i3, ok := <-c3
		if ok {
			fmt.Printf("received ", i3, " from c3\n")
		} else {
			fmt.Printf("c3 is closed\n")
		}
	default:
		fmt.Printf("no communication\n")
	}
}
