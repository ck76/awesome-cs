namespace Drawing {
    //如果我们需要在外部可以调用 SomeNameSpaceName 中的类和接口，则需要在类和接口添加 export 关键字。
    export interface IShape {
        draw();
    }
    export class Circle implements IShape {
        public draw() {
            console.log("Circle is drawn");
        }
    }
    export class Triangle implements IShape {
        public draw() {
            console.log("Triangle is drawn");
        }
    }

}
function drawAllShapes(shape:Drawing.IShape) {
    shape.draw();
}
drawAllShapes(new Drawing.Circle());
drawAllShapes(new Drawing.Triangle());



namespace Runoob {
    export namespace invoiceApp {
        export class Invoice {
            public calculateDiscount(price: number) {
                return price * .40;
            }
        }
    }
}
var invoice = new Runoob.invoiceApp.Invoice();
console.log(invoice.calculateDiscount(500));
