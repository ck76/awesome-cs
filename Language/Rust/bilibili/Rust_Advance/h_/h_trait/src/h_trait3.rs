//TODO 完全限定语法
//TODO 同名方法调用
//trait A {
//    fn print(&self);
//}
//
//trait B {
//    fn print(&self);
//}
//
//struct MyType;
//
//impl A for MyType {
//    fn print(&self) {
//        println!("A trait for MyType");
//    }
//}
//
//impl B for MyType {
//    fn print(&self) {
//        println!("B trait for MyType");
//    }
//}
//
//impl MyType {
//    fn print(&self) {
//        println!("MyType");
//    }
//}
//
//fn main() {
//    let my_type = MyType;
//    my_type.print(); //等价于MyType::print(&my_type);

//    A::print(&my_type);
//    B::print(&my_type);
//    println!("Hello, world!");
//}

//TODO 关联函数，没有self怎么办？ as 完全限定语法  //<Type as Trait>::function(.....)
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("baby_name: {}", Dog::baby_name());
    //println!("baby_name: {}", Animal::baby_name()); //error
    println!("baby_name: {}", <Dog as Animal>::baby_name()); //完全限定语法
}

//完全限定语法定义：
//<Type as Trait>::function(.....)
