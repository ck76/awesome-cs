////1、 指针是一个包含内存地址的变量。这个地址指向一些其它的数据。
//
//智能指针是一类数据结构，它们表现类似于指针，但是也拥有额外的元数据，最明显的，它们拥有一个引用
//计数。引用计数记录智能指针总共有多少个所有者，并且当没有任何所有者时清除数据
////
//普通引用和智能指针的一个额外区别是:引用只是只借用数据的指针，而智能指针则是拥有它们指向的数据
////
////2、 智能指针通常使用结构体实现。智能指针区别于常规结构体的显著特征在于其实现了Deref和Drop trait。
//// (1) Deref trait允许智能指针结构体实例表现的像引用一样，这样就可以编写即用于引用，又用于智能指针的代
////(2)Droptrait允许我们自定义当智能指针离开作用域时执行的代码。
////
////3、 几个标准库中的智能指针:
////Box<T>,用于在堆上分配
////Rc<T>, 一个引用计数类型，其数据可以有多个所有者;
////Ref<T>和RefMut<T>, 通过RefCell<T访问>, 一个在运行时而不是在编译时执行借用规则的类型。
fn main() {
    println!("Hello, world!");
}
