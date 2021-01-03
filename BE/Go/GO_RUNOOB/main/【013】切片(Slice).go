package main

//Go 语言切片是对数组的抽象。
//Go 数组的长度不可改变，在特定场景中这样的集合就不太适用，
// Go中提供了一种灵活，功能强悍的内置类型切片("动态数组"),与数组相比切片的长度是不固定的，可以追加元素，在追加时可能使切片的容量增大。
import "fmt"

func main() {
	numbers := []int{0, 1, 2, 3, 4, 5, 6, 7, 8}
	printSlice(numbers)
	fmt.Println("numbers ==", numbers)
	numbers1 := numbers[1:4]
	printSlice(numbers1)
	fmt.Println("numbers[:3] ==", numbers[:3])
	numbers2 := numbers[4:]
	printSlice(numbers2)
	numbers3 := make([]int, 0, 5)
	printSlice(numbers3)
	numbers4 := numbers[:2]
	printSlice(numbers4)
}

func printSlice(x []int) {
	//我们可以看出切片，实际的是获取数组的某一部分，len切片<=cap切片<=len数组，切片由三部分组成：指向底层数组的指针、len、cap。
	fmt.Printf("len=%d cap=%d slice=%v\n", len(x), cap(x), x)
//	len=9 cap=9 slice=[0 1 2 3 4 5 6 7 8]
	//numbers == [0 1 2 3 4 5 6 7 8]
	//len=3 cap=8 slice=[1 2 3]
	//numbers[:3] == [0 1 2]
	//len=5 cap=5 slice=[4 5 6 7 8]
	//len=0 cap=5 slice=[]
	//len=2 cap=9 slice=[0 1]
}
