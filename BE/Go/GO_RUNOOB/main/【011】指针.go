package main

import "fmt"

func main() {
	var a int = 10
	fmt.Printf("a 变量的地址: %x\n", &a)

	pointer()
	pointer_array()
	pointer_to_pointer()
	pointer_as_arguments()
}

func pointer() {
	//var ip *int        /* 指向整型*/
	//var fp *float32    /* 指向浮点型 */

	var a int = 20 /* 声明实际变量 */
	var ip *int    /* 声明指针变量 */

	ip = &a /* 指针变量的存储地址 */

	fmt.Printf("a 变量的地址: %x\n", &a)

	/* 指针变量的存储地址 */
	fmt.Printf("ip 变量储存的指针地址: %x\n", ip)

	/* 使用指针访问值 */
	fmt.Printf("*ip 变量的值: %d\n", *ip)

	//	TODO 空指针
	//	if(ptr != nil)     /* ptr 不是空指针 */
	//	if(ptr == nil)    /* ptr 是空指针 */
}

//TODO 指针数组  创建指针数组的时候，不适合用 range 循环
const max = 3

func pointer_array() {
	pointer_array_ture()
	pointer_array_false()
}

func pointer_array_false() {
	number := [max]int{5, 6, 7}
	var ptrs [max]*int //指针数组
	//将number数组的值的地址赋给ptrs
	for i, x := range &number {
		ptrs[i] = &x
	}
	for i, x := range ptrs {
		fmt.Printf("false 指针数组：索引:%d 值:%d 值的内存地址:%d\n", i, *x, x)
	}
}
func pointer_array_ture() {
	number := [max]int{5, 6, 7}
	var ptrs [max]*int //指针数组
	//将number数组的值的地址赋给ptrs
	for i := 0; i < max; i++ {
		ptrs[i] = &number[i]
	}
	for i, x := range ptrs {
		fmt.Printf("ture 指针数组：索引:%d 值:%d 值的内存地址:%d\n", i, *x, x)
	}
}

//TODO 指向指针的指针
func pointer_to_pointer(){
	var a int = 1
	var ptr1 *int = &a
	var ptr2 **int = &ptr1
	var ptr3 **(*int) = &ptr2 // 也可以写作：var ptr3 ***int = &ptr2
	// 依次类推
	fmt.Println("a:", a)
	fmt.Println("ptr1", ptr1)
	fmt.Println("ptr2", ptr2)
	fmt.Println("ptr3", ptr3)
	fmt.Println("*ptr1", *ptr1)
	fmt.Println("**ptr2", **ptr2)
	fmt.Println("**(*ptr3)", **(*ptr3)) // 也可以写作：***ptr3

	var a2 int = 5
	//把ptr指针 指向ss所在地址
	var ptr *int = &a2
	//开辟一个新的指针，指向ptr指针指向的地方
	var pts *int = ptr
	//二级指针，指向一个地址，这个地址存储的是一级指针的地址
	var pto **int = &ptr
	//三级指针，指向一个地址，这个地址存储的是二级指针的地址，二级指针同上
	var pt3 ***int = &pto
	fmt.Println("a的地址:",&a,
		"\n 值", a, "\n\n",

		"ptr指针所在地址:",&ptr,
		"\n ptr指向的地址:",ptr,
		"\n ptr指针指向地址对应的值",*ptr,"\n\n",

		"pts指针所在地址:",&pts,
		"\n pts指向的地址:", pts,
		"\n pts指针指向地址对应的值:",*pts,"\n\n",

		"pto指针所在地址:",&pto,
		"\n pto指向的指针（ptr）的存储地址:",pto,
		"\n pto指向的指针（ptr）所指向的地址: " ,*pto,
		"\n pto最终指向的地址对应的值（a）",**pto,"\n\n",

		"pt3指针所在的地址:",&pt3,
		"\n pt3指向的指针（pto）的地址:",pt3,//等于&*pt3,
		"\n pt3指向的指针（pto）所指向的指针的（ptr）地址", *pt3, //等于&**pt3,
		"\n pt3指向的指针（pto）所指向的指针（ptr）所指向的地址（a）:",**pt3, //等于&***pt3,
		"\n pt3最终指向的地址对应的值（a）", ***pt3)
}

//TODO 指针作为函数参数
func pointer_as_arguments(){
	/* 定义局部变量 */
	var a int = 100
	var b int= 200
	swap(&a, &b);

	fmt.Printf("交换后 a 的值 : %d\n", a )
	fmt.Printf("交换后 b 的值 : %d\n", b )
}

func swap(x *int, y *int) {
	//	*x, *y = *y, *x

	var temp int
	temp = *x    /* 保存 x 地址的值 */
	*x = *y      /* 将 y 赋值给 x */
	*y = temp    /* 将 temp 赋值给 y */
}
