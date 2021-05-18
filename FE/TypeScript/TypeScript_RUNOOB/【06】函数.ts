//TODO 带参数
function add(x: number, y: number): number {
    return x + y;
}

console.log(add(1, 2))

//-------------------------------------------------------------
//TODO 可选参数和默认参数
function buildName(firstName: string, lastName: string, midName?: string, defaultName = "chengkun", ...restName: string[]): string {
    return firstName + " " + lastName;
}

// let result1 = buildName("Bob");                  // 错误，缺少参数
// let result2 = buildName("Bob", "Adams", "Sr.");  // 错误，参数太多了
let result3 = buildName("Bob", "Adams", "midName", "defaultName", "rest1", "rest2");         // 正确

//-------------------------------------------------------------
//TODO 匿名函数
var msg = function () {
    return "hello world";
};

//-------------------------------------------------------------
//TODO 匿名函数自调用
(function (s) {
    var x = "Hello!! " + s;
    console.log(x)
})("hhhhhhhh");

//-------------------------------------------------------------
//TODO 构造函数
var myFunction = new Function("a", "b", "return a * b");
var x = myFunction(4, 3);
console.log(x);

//-------------------------------------------------------------
//TODO 递归函数
var result = function factorial(number) {
    if (number <= 0) {         // 停止执行
        return 1;
    } else {
        return (number * factorial(number - 1));     // 调用自身
    }
}(6);
console.log(result);

//-------------------------------------------------------------
//TODO Lambda 函数（箭头函数）
var foo = (x: number) => 10 + x
console.log(foo(100))      //输出结果为 110
var foo2 = (x: number) => {
    x = 10 + x
    console.log(x)
}
foo2(100)

//单个参数 () 是可选的：
var display = x => {
    console.log("输出为 "+x)
}
display(12)
//无参数时可以设置空括号：
var display_0 =()=> {
    console.log("Function invoked");
}
display_0();

//-------------------------------------------------------------
//TODO 函数重载
function disp(s1:string):void;
function disp(n1:number,s1:string):void;

function disp(x:any,y?:any):void {
    console.log(x);
    console.log(y);
}
disp("abc")
disp(1,"xyz");
