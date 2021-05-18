//TODO 带参数
function add(x, y) {
    return x + y;
}
console.log(add(1, 2));
//TODO 可选参数和默认参数
function buildName(firstName, lastName, midName, defaultName) {
    if (defaultName === void 0) { defaultName = "chengkun"; }
    var restName = [];
    for (var _i = 4; _i < arguments.length; _i++) {
        restName[_i - 4] = arguments[_i];
    }
    return firstName + " " + lastName;
}
// let result1 = buildName("Bob");                  // 错误，缺少参数
// let result2 = buildName("Bob", "Adams", "Sr.");  // 错误，参数太多了
var result3 = buildName("Bob", "Adams", "midName", "defaultName", "rest1", "rest2"); // 正确
//TODO 匿名函数
var msg = function () {
    return "hello world";
};
//TODO 匿名函数自调用
(function (s) {
    var x = "Hello!! " + s;
    console.log(x);
})("hhhhhhhh");
//TODO 构造函数
var myFunction = new Function("a", "b", "return a * b");
var x = myFunction(4, 3);
console.log(x);
//TODO 递归函数
var result = function factorial(number) {
    if (number <= 0) { // 停止执行
        return 1;
    }
    else {
        return (number * factorial(number - 1)); // 调用自身
    }
}(6);
console.log(result);
//TODO Lambda 函数（箭头函数）
var foo = function (x) { return 10 + x; };
console.log(foo(100)); //输出结果为 110
var foo2 = function (x) {
    x = 10 + x;
    console.log(x);
};
foo2(100);
//单个参数 () 是可选的：
var display = function (x) {
    console.log("输出为 " + x);
};
display(12);
//无参数时可以设置空括号：
var display_0 = function () {
    console.log("Function invoked");
};
display_0();
function disp(x, y) {
    console.log(x);
    console.log(y);
}
disp("abc");
disp(1, "xyz");
