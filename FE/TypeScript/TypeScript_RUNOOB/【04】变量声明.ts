//TODO 类型断言
var str = '1'
var str2: number = <number><any>str   //str、str2 是 string 类型
var str3: number = str as any as number
console.log(str2)

//-------------------------------------------------------------

//TODO 变量作用域
//全局作用域 − 全局变量定义在程序结构的外部，它可以在你代码的任何位置使用。
// 类作用域 − 这个变量也可以称为 字段。类变量声明在一个类里头，但在类的方法外面。 该变量可以通过类的对象来访问。类变量也可以是静态的，静态的变量可以通过类名直接访问。
// 局部作用域 − 局部变量，局部变量只能在声明它的一个代码块（如：方法）中使用。

var global_num = 12          // 全局变量
class Numbers {
    num_val = 13;             // 实例变量
    static sval = 10;         // 静态变量

    storeNum():void {
        var local_num = 14;    // 局部变量
    }
}
console.log("全局变量为: "+global_num)
console.log(Numbers.sval)   // 静态变量
var obj = new Numbers();
console.log("实例变量: "+obj.num_val)
