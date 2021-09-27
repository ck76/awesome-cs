package main

import "fmt"

func main() {
	for_for()
	goto_()
}

func for_for() {
	/* 定义局部变量 */
	var i, j int

	for i = 2; i < 100; i++ {
		for j = 2; j <= (i / j); j++ {
			if (i%j == 0) {
				break; // 如果发现因子，则不是素数
			}
		}
		if (j > (i / j)) {
			fmt.Printf("%d  是素数\n", i);
		}
	}
}
func goto_() {
	/* 定义局部变量 */
	var a int = 10

	/* 循环 */
LOOP:
	for a < 20 {
		if a == 15 {
			/* 跳过迭代 */
			a = a + 1
			goto LOOP
		}
		fmt.Printf("a的值为 : %d\n", a)
		a++
	}
}
