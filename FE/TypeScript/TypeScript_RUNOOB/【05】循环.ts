//-------------------------------------------------------------

//todo for in
var j:any;
var n:any = "a b c"

for(j in n) {
    console.log(n[j])
}

//TypeScript 还支持 for…of 、forEach、every 和 some 循环。
// for...of 语句创建一个循环来迭代可迭代的对象。
// 在 ES6 中引入的 for...of 循环，以替代 for...in 和 forEach() ，支持新的迭代协议。
// for...of 允许你遍历 Arrays（数组）, Strings（字符串）, Maps（映射）, Sets（集合）等可迭代的数据结构等
//-------------------------------------------------------------

//todo for...of 循环
let someArray = [1, "string", false];

for (let entry of someArray) {
    console.log(entry); // 1, "string", false
}
//-------------------------------------------------------------

//todo forEach 循环
let list = [4, 5, 6];
list.forEach((val, idx, array) => {
    // val: 当前值
    // idx：当前index
    // array: Array
});
//-------------------------------------------------------------

//todo every 循环
let list2 = [4, 5, 6];
list2.every((val, idx, array) => {
    // val: 当前值
    // idx：当前index
    // array: Array
    return true; // Continues
    // Return false will quit the iteration
});
