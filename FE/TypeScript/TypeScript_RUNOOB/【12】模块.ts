

//TypeScript 模块的设计理念是可以更换的组织代码。
//
// 模块是在其自身的作用域里执行，并不是在全局作用域，这意味着定义在模块里面的变量、函数和类等在模块外部是不可见的，除非明确地使用 export 导出它们。
// 类似地，我们必须通过 import 导入其他模块导出的变量、函数、类等。
//
// 两个模块之间的关系是通过在文件级别上使用 import 和 export 建立的。
//
// 模块使用模块加载器去导入其它的模块。 在运行时，模块加载器的作用是在执行此模块代码前去查找并执行这个模块的所有依赖。
// 大家最熟知的JavaScript模块加载器是服务于 Node.js 的 CommonJS 和服务于 Web 应用的 Require.js。
//
// 此外还有有 SystemJs 和 Webpack。
import shape = require("./ckmod");
export class Circle implements shape.IShape {
    public draw() {
        console.log("Cirlce is drawn (external module)");
    }
}
