package main

import "fmt"

func main() {
	language()
	relation()
	logic()
	bit()
	assignment()
	other()
	priority()
}

func language() {
	var a int = 21
	var b int = 10
	var c int

	c = a + b
	fmt.Printf("第一行 - c 的值为 %d\n", c)
	c = a - b
	fmt.Printf("第二行 - c 的值为 %d\n", c)
	c = a * b
	fmt.Printf("第三行 - c 的值为 %d\n", c)
	c = a / b
	fmt.Printf("第四行 - c 的值为 %d\n", c)
	c = a % b
	fmt.Printf("第五行 - c 的值为 %d\n", c)
	a++
	fmt.Printf("第六行 - a 的值为 %d\n", a)
	a = 21 // 为了方便测试，a 这里重新赋值为 21
	a--
	fmt.Printf("第七行 - a 的值为 %d\n", a)
	//	第一行 - c 的值为 31
	//第二行 - c 的值为 11
	//第三行 - c 的值为 210
	//第四行 - c 的值为 2
	//第五行 - c 的值为 1
	//第六行 - a 的值为 22
	//第七行 - a 的值为 20
}

func relation() {
	var a int = 21
	var b int = 10

	if (a == b) {
		fmt.Printf("第一行 - a 等于 b\n")
	} else {
		fmt.Printf("第一行 - a 不等于 b\n")
	}
	if (a < b) {
		fmt.Printf("第二行 - a 小于 b\n")
	} else {
		fmt.Printf("第二行 - a 不小于 b\n")
	}

	if (a > b) {
		fmt.Printf("第三行 - a 大于 b\n")
	} else {
		fmt.Printf("第三行 - a 不大于 b\n")
	}
	/* Lets change value of a and b */
	a = 5
	b = 20
	if (a <= b) {
		fmt.Printf("第四行 - a 小于等于 b\n")
	}
	if (b >= a) {
		fmt.Printf("第五行 - b 大于等于 a\n")
	}
	//	第一行 - a 不等于 b
	//第二行 - a 不小于 b
	//第三行 - a 大于 b
	//第四行 - a 小于等于 b
	//第五行 - b 大于等于 a
}

func logic() {
	var a bool = true
	var b bool = false
	if (a && b) {
		fmt.Printf("第一行 - 条件为 true\n")
	}
	if (a || b) {
		fmt.Printf("第二行 - 条件为 true\n")
	}
	/* 修改 a 和 b 的值 */
	a = false
	b = true
	if (a && b) {
		fmt.Printf("第三行 - 条件为 true\n")
	} else {
		fmt.Printf("第三行 - 条件为 false\n")
	}
	if (!(a && b)) {
		fmt.Printf("第四行 - 条件为 true\n")
	}
	//	第二行 - 条件为 true
	//第三行 - 条件为 false
	//第四行 - 条件为 true
}

func bit() {
	var a uint = 60 /* 60 = 0011 1100 */
	var b uint = 13 /* 13 = 0000 1101 */
	var c uint = 0

	c = a & b /* 12 = 0000 1100 */
	fmt.Printf("第一行 - c 的值为 %d\n", c)

	c = a | b /* 61 = 0011 1101 */
	fmt.Printf("第二行 - c 的值为 %d\n", c)

	c = a ^ b /* 49 = 0011 0001 */
	fmt.Printf("第三行 - c 的值为 %d\n", c)

	c = a << 2 /* 240 = 1111 0000 */
	fmt.Printf("第四行 - c 的值为 %d\n", c)

	c = a >> 2 /* 15 = 0000 1111 */
	fmt.Printf("第五行 - c 的值为 %d\n", c)
	//	第一行 - c 的值为 12
	//第二行 - c 的值为 61
	//第三行 - c 的值为 49
	//第四行 - c 的值为 240
	//第五行 - c 的值为 15
}

func assignment() {
	var a int = 21
	var c int

	c = a
	fmt.Printf("第 1 行 - =  运算符实例，c 值为 = %d\n", c)

	c += a
	fmt.Printf("第 2 行 - += 运算符实例，c 值为 = %d\n", c)

	c -= a
	fmt.Printf("第 3 行 - -= 运算符实例，c 值为 = %d\n", c)

	c *= a
	fmt.Printf("第 4 行 - *= 运算符实例，c 值为 = %d\n", c)

	c /= a
	fmt.Printf("第 5 行 - /= 运算符实例，c 值为 = %d\n", c)

	c = 200;
	c <<= 2
	fmt.Printf("第 6行  - <<= 运算符实例，c 值为 = %d\n", c)

	c >>= 2
	fmt.Printf("第 7 行 - >>= 运算符实例，c 值为 = %d\n", c)

	c &= 2
	fmt.Printf("第 8 行 - &= 运算符实例，c 值为 = %d\n", c)

	c ^= 2
	fmt.Printf("第 9 行 - ^= 运算符实例，c 值为 = %d\n", c)

	c |= 2
	fmt.Printf("第 10 行 - |= 运算符实例，c 值为 = %d\n", c)

	//	第 1 行 - =  运算符实例，c 值为 = 21
	//第 2 行 - += 运算符实例，c 值为 = 42
	//第 3 行 - -= 运算符实例，c 值为 = 21
	//第 4 行 - *= 运算符实例，c 值为 = 441
	//第 5 行 - /= 运算符实例，c 值为 = 21
	//第 6行  - <<= 运算符实例，c 值为 = 800
	//第 7 行 - >>= 运算符实例，c 值为 = 200
	//第 8 行 - &= 运算符实例，c 值为 = 0
	//第 9 行 - ^= 运算符实例，c 值为 = 2
	//第 10 行 - |= 运算符实例，c 值为 = 2
}

func other() {
	//&	返回变量存储地址	&a; 将给出变量的实际地址。
	//*	指针变量。	*a; 是一个指针变量
	var a int = 4
	var b int32
	var c float32
	var ptr *int

	/* 运算符实例 */
	fmt.Printf("第 1 行 - a 变量类型为 = %T\n", a);
	fmt.Printf("第 2 行 - b 变量类型为 = %T\n", b);
	fmt.Printf("第 3 行 - c 变量类型为 = %T\n", c);

	/*  & 和 * 运算符实例 */
	ptr = &a /* 'ptr' 包含了 'a' 变量的地址 */
	fmt.Printf("a 的值为  %d\n", a);
	fmt.Printf("*ptr 为 %d\n", *ptr);

	//	第 1 行 - a 变量类型为 = int
	//第 2 行 - b 变量类型为 = int32
	//第 3 行 - c 变量类型为 = float32
	//a 的值为  4
	//*ptr 为 4
}

func priority() {
	var a int = 20
	var b int = 10
	var c int = 15
	var d int = 5
	var e int;
	e = (a + b) * c / d; // ( 30 * 15 ) / 5
	fmt.Printf("(a + b) * c / d 的值为 : %d\n", e);
	e = ((a + b) * c) / d; // (30 * 15 ) / 5
	fmt.Printf("((a + b) * c) / d 的值为  : %d\n", e);
	e = (a + b) * (c / d); // (30) * (15/5)
	fmt.Printf("(a + b) * (c / d) 的值为  : %d\n", e);
	e = a + (b*c)/d; //  20 + (150/5)
	fmt.Printf("a + (b * c) / d 的值为  : %d\n", e);

	//	(a + b) * c / d 的值为 : 90
	//((a + b) * c) / d 的值为  : 90
	//(a + b) * (c / d) 的值为  : 90
	//a + (b * c) / d 的值为  : 50
}
