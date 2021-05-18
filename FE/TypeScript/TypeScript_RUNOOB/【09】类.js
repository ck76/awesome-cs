class Car {
    // 构造函数
    constructor(engine) {
        this.engine = engine;
    }
    // 方法
    disp() {
        console.log("函数中显示发动机型号  :   " + this.engine);
    }
}
// 创建一个对象
var obj = new Car("XXSY1");
// 访问字段
console.log("读取发动机型号 :  " + obj.engine);
// 访问方法
obj.disp();
//-------------------------------------------------------------
class Shape {
    constructor(a) {
        this.Area = a;
    }
}
class Circle extends Shape {
    disp() {
        console.log("圆的面积:  " + this.Area);
    }
}
var obj1 = new Circle(223);
obj1.disp();
//-------------------------------------------------------------
//todo 继承类的方法重写
class PrinterClass {
    doPrint() {
        console.log("父类的 doPrint() 方法。");
    }
}
class StringPrinter extends PrinterClass {
    doPrint() {
        super.doPrint(); // 调用父类的函数
        console.log("子类的 doPrint()方法。");
    }
}
//-------------------------------------------------------------
//todo static 关键字
class StaticMem {
    static disp() {
        console.log("num 值为 " + StaticMem.num);
    }
}
StaticMem.num = 12; // 初始化静态变量
StaticMem.disp(); // 调用静态方法
//-------------------------------------------------------------
//todo instanceof 运算符
class Person {
}
var obj11 = new Person();
var isPerson = obj11 instanceof Person;
console.log("obj11 对象是 Person 类实例化来的吗？ " + isPerson);
//-------------------------------------------------------------
//todo 访问控制修饰符
//public（默认） : 公有，可以在任何地方被访问。
// protected : 受保护，可以被其自身以及其子类和父类访问。
// private : 私有，只能被其定义所在的类访问。
class Encapsulate {
    constructor() {
        this.str1 = "hello";
        this.str2 = "world";
    }
}
var obj22 = new Encapsulate();
console.log(obj22.str1); // 可访问
class AgriLoan {
    constructor(interest, rebate) {
        this.interest = interest;
        this.rebate = rebate;
    }
}
var obj33 = new AgriLoan(10, 1);
console.log("利润为 : " + obj33.interest + "，抽成为 : " + obj33.rebate);
