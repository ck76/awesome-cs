//TypeScript 程序由以下几个部分组成：
//
// 模块
// 函数
// 变量
// 语句和表达式
// 注释
//tsc 常用编译参数如下表所示：
//
// 序号	编译参数说明
// 1.
// --help
// 显示帮助信息
//
// 2.
// --module
// 载入扩展模块
//
// 3.
// --target
// 设置 ECMA 版本
//
// 4.
// --declaration
// 额外生成一个 .d.ts 扩展名的文件。
//
// tsc ts-hw.ts --declaration
// 以上命令会生成 ts-hw.d.ts、ts-hw.js 两个文件。
//
// 5.
// --removeComments
// 删除文件的注释
//
// 6.
// --out
// 编译多个文件并合并到一个输出的文件
//
// 7.
// --sourcemap
// 生成一个 sourcemap (.map) 文件。
// sourcemap 是一个存储源代码与编译代码对应位置映射的信息文件。
//
// 8.
// --module noImplicitAny
// 在表达式和声明上有隐含的 any 类型时报错
//
// 9.
// --watch
// 在监视模式下运行编译器。会监视输出文件，在它们改变时重新编译。
//TODO TypeScript 面向对象编程实例：
var Site = /** @class */ (function () {
    function Site() {
    }
    Site.prototype.name = function () {
        console.log("chengkun");
    };
    return Site;
}());
var site = new Site();
site.name();
