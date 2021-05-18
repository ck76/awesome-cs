//---------------------------------------------------------------------------
//TODO Number
//TypeScript 与 JavaScript 类似，支持 Number 对象。
// Number 对象是原始数值的包装对象。
var num = new Number(19990804);
console.log("TypeScript Number 属性: ");
console.log("最大值为: " + Number.MAX_VALUE);
console.log("最小值为: " + Number.MIN_VALUE);
console.log("负无穷大: " + Number.NEGATIVE_INFINITY);
console.log("正无穷大:" + Number.POSITIVE_INFINITY);
//---------------------------------------------------------------------------
//TODO prototype 实例
function employee(id, name) {
    this.id = id;
    this.name = name;
}
var emp = new employee(123, "admin");
employee.prototype.email = "admin@runoob.com";
console.log("员工号: " + emp.id);
console.log("员工姓名: " + emp.name);
console.log("员工邮箱: " + emp.email);
//TODO Number的toXXX方法族
//---------------------------------------------------------------------------
//TODO String（字符串）
var txt = new String("string");
var txt2 = "string";
//
//---------------------------------------------------------------------------
//TODO Array(数组)
var sites;
sites = ["Google", "Runoob", "Taobao"];
//todo Array 对象
var arr_names = new Array(4);
for (var i = 0; i < arr_names.length; i++) {
    arr_names[i] = i * 2;
    console.log(arr_names[i]);
}
var sites = new Array("Google", "Runoob", "Taobao", "Facebook");
for (var i = 0; i < sites.length; i++) {
    console.log(sites[i]);
}
//TODO 数组解构
var arr = [12, 13];
var [x, y] = arr; // 将数组的两个元素赋值给变量 x 和 y
console.log(x);
console.log(y);
//todo 数组迭代
var nums = [1001, 1002, 1003, 1004];
for (var j in nums) {
    console.log(nums[j]);
}
//xxx方法族
//---------------------------------------------------------------------------
//TODO Map 对象
let mapa = new Map();
let myMap = new Map([
    ["key1", "value1"],
    ["key2", "value2"]
]);
//Map 相关的函数与属性：
//
// map.clear() – 移除 Map 对象的所有键/值对 。
// map.set() – 设置键值对，返回该 Map 对象。
// map.get() – 返回键对应的值，如果不存在，则返回 undefined。
// map.has() – 返回一个布尔值，用于判断 Map 中是否包含键对应的值。
// map.delete() – 删除 Map 中的元素，删除成功返回 true，失败返回 false。
// map.size – 返回 Map 对象键/值对的数量。
// map.keys() - 返回一个 Iterator 对象， 包含了 Map 对象中每个元素的键 。
// map.values() – 返回一个新的Iterator对象，包含了Map对象中每个元素的值 。
//todo 迭代 Map
for (let key of myMap.keys()) {
    console.log(key);
}
// 迭代 Map 中的 value
for (let value of myMap.values()) {
    console.log(value);
}
// 迭代 Map 中的 key => value
for (let entry of myMap.entries()) {
    console.log(entry[0], entry[1]);
}
// 使用对象解析
for (let [key, value] of myMap) {
    console.log(key, value);
}
//---------------------------------------------------------------------------
// TODO 元组
var mytuple1 = [10, "Runoob"];
var mytuple = [];
mytuple[0] = 120;
mytuple[1] = 234;
//元祖运算
//push() 向元组添加元素，添加在最后面。
// pop() 从元组中移除元素（最后一个），并返回移除的元素。
var [b, c] = mytuple; //解构
//---------------------------------------------------------------------------
//TODO 联合类型
var val;
val = 12;
console.log("数字为 " + val);
val = "Runoob";
console.log("字符串为 " + val);
//联合类型函数参数
function disp(name) {
    if (typeof name == "string") {
        console.log(name);
    }
    else {
        var i;
        for (i = 0; i < name.length; i++) {
            console.log(name[i]);
        }
    }
}
disp("Runoob");
console.log("输出数组....");
disp(["Runoob", "Google", "Taobao", "Facebook"]);
//联合类型数组
var arr_x;
var i;
arr_x = [1, 2, 4];
console.log("**数字数组**");
for (i = 0; i < arr_x.length; i++) {
    console.log(arr_x[i]);
}
arr_x = ["Runoob", "Google", "Taobao"];
console.log("**字符串数组**");
for (i = 0; i < arr_x.length; i++) {
    console.log(arr_x[i]);
}
