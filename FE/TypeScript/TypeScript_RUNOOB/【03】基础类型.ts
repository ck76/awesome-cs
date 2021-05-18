//TODO 任意类型
var anyyyy: any = "aa";
anyyyy = 1;
//-------------------------------------------------------------

//TODO 字符串
let nickname: string = "chengkun";
let years: number = 5;
let words: string = `您好，今年是 ${nickname} 发布 ${years + 1} 周年`;
//-------------------------------------------------------------

//TODO boolean
let flag: boolean = true;
//-------------------------------------------------------------

//TODO 数组
// 在元素类型后面加上[]
let arr: number[] = [1, 2];
// 或者使用数组泛型
let arr2: Array<number> = [1, 2];
//-------------------------------------------------------------

//TODO 元祖
let x: [string, number];
let y = [1, 2, 3, "4", [5]]
x = ['Runoob', 1];    // 运行正常
// x = [1, 'Runoob'];    // 报错
console.log(x[0]);    // 输出 Runoob
//-------------------------------------------------------------

//TODO 枚举
enum Color {Red, Blue, Black}

let color: Color = Color.Blue;
console.log(color);    // 输出 2

const getValue = () => {
    return 0
}

enum List {
    A = getValue(),
    B = 2,  // 此处必须要初始化值，不然编译不通过
    C
}

console.log(List.A) // 0
console.log(List.B) // 2
console.log(List.C) // 3
//-------------------------------------------------------------

//TODO void
function hello(): void {
    alert("Hello Runoob");
}
//-------------------------------------------------------------

//TODO Null 和 Undefined
//null 在 JavaScript 中 null 表示 "什么都没有"。
// null是一个只有一个值的特殊类型。表示一个空对象引用。
// 用 typeof 检测 null 返回是 object。
//
// undefined
// 在 JavaScript 中, undefined 是一个没有设置值的变量。
// typeof 一个没有值的变量会返回 undefined。
//
// Null 和 Undefined 是其他任何类型（包括 void）的子类型，可以赋值给其它类型，
// 如数字类型，此时，赋值后的类型会变成 null 或 undefined。
// 而在TypeScript中启用严格的空校验（--strictNullChecks）特性，
// 就可以使得null 和 undefined 只能被赋值给 void 或本身对应的类型，示例代码如下：


// 启用 --strictNullChecks
let x1: number;
x1 = 1; // 运行正确
x1 = undefined;    // 运行错误
x1 = null;    // 运行错误


let x2: number | null | undefined;
x2 = 1; // 运行正确
x2 = undefined;    // 运行正确
x2 = null;    // 运行正确
//-------------------------------------------------------------

//TODO never 类型
//never 是其它类型（包括 null 和 undefined）的子类型，代表从不会出现的值。
// 这意味着声明为 never 类型的变量只能被 never 类型所赋值，
// 在函数中它通常表现为抛出异常或无法执行到终止点（例如无限循环），示例代码如下：
let x_never: never;
let y_number: number;

// 运行错误，数字类型不能转为 never 类型
// x_never = 123;

// 运行正确，never 类型可以赋值给 never类型
x_never = (() => {
    throw new Error('exception')
})();

// 运行正确，never 类型可以赋值给 数字类型
y_number = (() => {
    throw new Error('exception')
})();

// 返回值为 never 的函数可以是抛出异常的情况
function error(message: string): never {
    throw new Error(message);
}

// 返回值为 never 的函数可以是无法被执行到的终止点的情况
function loop(): never {
    while (true) {

    }
}
