
exports.world=function () {
    console.log('Hello World');
};
exports.cc="chengkun";

//##############################################3
//有时候我们只是想把一个对象封装到模块中，格式如下
function Hello() {
    var name;
    this.setName = function(thyName) {
        name = thyName;
    };
    this.sayHello = function() {
        console.log('Hello ' + name);
    };
};
module.exports = Hello;
//模块接口的唯一变化是使用 module.exports = Hello 代替了exports.world = function(){}。
//  在外部引用该模块时，其接口对象就是要输出的 Hello 对象本身，而不是原先的 exports。



//exports 和 module.exports 的使用
// 如果要对外暴露属性或方法，就用 exports 就行，
// 要暴露对象(类似class，包含了很多属性和方法)，就用 module.exports。
