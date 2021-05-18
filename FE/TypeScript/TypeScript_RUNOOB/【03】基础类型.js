//TODO 任意类型
var anyyyy = "aa";
anyyyy = 1;
//TODO 字符串
var nickname = "chengkun";
var years = 5;
var words = "\u60A8\u597D\uFF0C\u4ECA\u5E74\u662F " + nickname + " \u53D1\u5E03 " + (years + 1) + " \u5468\u5E74";
//TODO boolean
var flag = true;
//TODO 数组
// 在元素类型后面加上[]
var arr = [1, 2];
// 或者使用数组泛型
var arr2 = [1, 2];
//TODO 元祖
var x;
var y = [1, 2, 3, "4", [5]];
x = ['Runoob', 1]; // 运行正常
// x = [1, 'Runoob'];    // 报错
console.log(x[0]); // 输出 Runoob
//TODO 枚举
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Blue"] = 1] = "Blue";
    Color[Color["Black"] = 2] = "Black";
})(Color || (Color = {}));
var color = Color.Blue;
console.log(color); // 输出 2
//TODO void
function hello() {
    alert("Hello Runoob");
}
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
var x1;
x1 = 1; // 运行正确
x1 = undefined; // 运行错误
x1 = null; // 运行错误
