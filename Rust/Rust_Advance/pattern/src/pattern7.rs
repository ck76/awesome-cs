////TODO 6、忽略模式中的值_ ,_ ,
//fn foo(_: i32, y: i32) {
//    println!("y = {}", y);
//}
//
////trait A {
////    fn bar(x: i32, y: i32);
////}
////
////struct B {}
////
////impl A for B {
////    fn bar(_: i32, y: i32) {
////        println!("y = {}", y);
////    }
////}

//TODO 忽略部分值
//fn main() {
//    foo(1, 2);
//
//    let numbers = (1, 2, 3, 4);
//    match numbers {
//        (one, _, three, _) => {
//            println!("one: {}, three: {}", one, three);
//        },
//    }
//    println!("Hello, world!");
//}


fn main() {
    let _x = 5;
    let _y = 5;

    //let s = Some(String::from("hello"));
    //if let Some(_c) = s { //TODO 不加_的话相当于s的所有权转移，加_相当于忽略变量但是还是会有所有权转移
    ////if let Some(c) = s {
    //    println!("found a string");
    //}
    ////println!("s: {:?}", s);

    let s = Some(String::from("hello"));
    if let Some(_) = s {//TODO 单纯一个 _ 的时候不会有所有权转移
        println!("found a string");
    }
    println!("s: {:?}", s);
}
