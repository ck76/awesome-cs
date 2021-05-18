//对象是包含一组键值对的实例。 值可以是标量、函数、数组、对象等，如下实例：
//-------------------------------------------------------------
//todo 类型模板
var sites = {
    site1: "Runoob",
    site2: "Google",
    sayHello: function () { },
    sayNull: function (s) { return 100; }
};
sites.sayHello = function () {
    console.log("hello " + sites.site1);
};
sites.sayNull = function (s) {
    return 1000000;
};
sites.sayHello();
sites.sayNull("cje");
function addPoints(p1, p2) {
    var x = p1.x + p2.x;
    var y = p1.y + p2.y;
    return { x: x, y: y };
}
// 正确
var newPoint = addPoints({ x: 3, y: 4 }, { x: 5, y: 1 });
// 错误
// var newPoint2 = addPoints({x:1},{x:4,y:3})
